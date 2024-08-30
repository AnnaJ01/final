import os
from bs4 import BeautifulSoup
import requests
import tkinter as tk                  
from tkinter import filedialog         
from tkinter import simpledialog      
import customtkinter as ctk


# Define a custom dialog class for numeric input with customtkinter
class NumericInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.result = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the entry field for numeric input
        self.numeric_entry = ctk.CTkEntry(self, width=350)
        self.numeric_entry.pack(pady=5, padx=20, fill=tk.X)
        self.numeric_entry.focus_set()
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        self.result = self.numeric_entry.get()
        self.destroy()

# Function to create and use the custom numeric input dialog
def ask_numeric(prompt):
    dialog = NumericInputDialog(root, prompt)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.result

# Initialize the Tkinter root window
root = ctk.CTk()
root.geometry("600x400")
root.title("Main Application")



# Define a custom dialog class for password input with customtkinter
class PasswordInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.result = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the entry field with password masking
        self.password_entry = ctk.CTkEntry(self, width=350, show='*')
        self.password_entry.pack(pady=5, padx=20, fill=tk.X)
        self.password_entry.focus_set()
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        self.result = self.password_entry.get()
        self.destroy()

# Function to create and use the custom password input dialog
def ask_password(prompt):
    dialog = PasswordInputDialog(root, prompt)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.result

# Initialize the Tkinter root window
root = ctk.CTk()
root.geometry("600x400")
root.title("Main Application")



# Define a custom dialog class for username input with customtkinter
class UsernameInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.result = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the entry field
        self.username_entry = ctk.CTkEntry(self, width=350)
        self.username_entry.pack(pady=5, padx=20, fill=tk.X)
        self.username_entry.focus_set()
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        self.result = self.username_entry.get()
        self.destroy()

# Function to create and use the custom username input dialog
def ask_username(prompt):
    dialog = UsernameInputDialog(root, prompt)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.result

# Initialize the Tkinter root window
root = ctk.CTk()
root.geometry("600x400")
root.title("Main Application")


# Define a custom dialog class for URL input with customtkinter
class URLInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.result = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the entry field
        self.url_entry = ctk.CTkEntry(self, width=350)
        self.url_entry.pack(pady=5, padx=20, fill=tk.X)
        self.url_entry.focus_set()
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        self.result = self.url_entry.get()
        self.destroy()

# Function to create and use the custom URL input dialog
def ask_url(prompt):
    dialog = URLInputDialog(root, prompt)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.result

# Initialize the Tkinter root window
root = ctk.CTk()
root.geometry("600x400")
root.title("Main Application")



# Define a custom dialog class for file selection with customtkinter
class FileSelectDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt, filetypes):
        super().__init__(parent)
        self.title("Select File")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.filetypes = filetypes
        self.file_path = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the "Browse" button
        self.browse_button = ctk.CTkButton(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)

    def browse_file(self):
        file_selected = filedialog.askopenfilename(title="Select File", filetypes=self.filetypes)
        if file_selected:
            self.file_path = file_selected
            # Print the file path for debugging (can be removed later)
            print(f"Selected file path: {file_selected}")

    def on_ok(self):
        self.destroy()

# Function to create and use the custom file selection dialog
def ask_file(prompt, filetypes):
    dialog = FileSelectDialog(root, prompt, filetypes)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.file_path

# Initialize the Tkinter root window
root = ctk.CTk()
root.geometry("600x400")
root.title("Main Application")

class FolderSelectDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Select Folder")
        self.geometry("400x200")
        
        self.prompt = prompt
        self.folder_path = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the "Browse" button
        self.browse_button = ctk.CTkButton(self, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=10)
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def browse_folder(self):
        folder_selected = filedialog.askdirectory(title="Select Folder")
        if folder_selected:
            self.folder_path = folder_selected
            # Optionally, you can display a confirmation message or status in the dialog
            # For example, use a label to show the selected path if desired

    def on_ok(self):
        self.destroy()

# Function to create and use the custom folder selection dialog
def ask_directory(prompt):
    dialog = FolderSelectDialog(root, prompt)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.folder_path



class ModernDialog(ctk.CTkToplevel):
    def __init__(self, parent, prompt, show=None):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x150")
        
        self.prompt = prompt
        self.show = show
        self.result = None
        
        # Create and pack the prompt label
        self.prompt_label = ctk.CTkLabel(self, text=self.prompt)
        self.prompt_label.pack(pady=10)
        
        # Create and pack the entry field
        self.entry = ctk.CTkEntry(self, show=self.show)  # Apply masking if needed
        self.entry.pack(pady=5, padx=20, fill=tk.X)
        self.entry.focus_set()
        
        # Create and pack the OK button
        self.ok_button = ctk.CTkButton(self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)
        
    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

# Function to create and use the custom dialog
def ask_input(prompt, show=None):
    dialog = ModernDialog(root, prompt, show)
    root.wait_window(dialog)  # Wait until the dialog is closed
    return dialog.result

# Initialize the Tkinter root window
root = ctk.CTk()  # Use customtkinter's CTk class for the root window
root.geometry("600x400")
root.title("Main Application")


def extract_images_and_captions(html_path, output_dir):
    """
    Extracts images and their captions from an HTML file.
    Saves images to a specified output directory and returns a list of tuples (image_path, caption).

    Args:
        html_path: Path to the HTML file.
        output_dir: Directory to save extracted images.

    Returns:
        A list of tuples (image_path, caption).
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"Output directory created or already exists: {output_dir}")

    pairs = []

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Successfully read HTML file: {html_path}")
    except Exception as e:
        print(f"Failed to read the HTML file: {e}")
        return pairs

    soup = BeautifulSoup(content, 'html.parser')

    images = soup.find_all('img')
    image_paragraphs = soup.find_all('p')

    captions = []
    found_first_image = False

    for paragraph in image_paragraphs:
        img_tag = paragraph.find('img')
        
        if img_tag:
            span_tags = paragraph.find_all('span')
            if len(span_tags) > 1:
                if found_first_image:
                    caption_text = ' '.join(span.get_text(strip=True) for span in span_tags)
                    if caption_text:
                        captions.append(caption_text)
                else:
                    found_first_image = True
            else:
                if found_first_image:
                    next_p = paragraph.find_next_sibling('p')
                    if next_p:
                        caption_text = next_p.get_text(strip=True)
                        captions.append(caption_text)
                else:
                    found_first_image = True

    # Start processing from the second image
    for idx, img in enumerate(images, start=1):
        img_src = img.get('src', None)
        if not img_src:
            print(f"Image {idx} has no 'src' attribute.")
            continue

        # Skip caption for the first image
        caption = None
        if idx > 1 and (idx-2) < len(captions):
            caption = captions[idx-2]
        
        print(f"Processing image {idx}: {img_src} with caption {caption}")

        try:
            abs_image_path = None
            image_data = None

            if img_src.startswith('http://') or img_src.startswith('https://'):
                response = requests.get(img_src)
                response.raise_for_status()
                image_data = response.content
            else:
                abs_image_path = os.path.abspath(os.path.join(os.path.dirname(html_path), img_src))
                if not os.path.exists(abs_image_path):
                    print(f"File not found: {abs_image_path}")
                    continue
                with open(abs_image_path, 'rb') as img_file:
                    image_data = img_file.read()

            if image_data:
                image_name = f'image_{idx}.jpg'
                image_path = os.path.join(output_dir, image_name)
                with open(image_path, 'wb') as f:
                    f.write(image_data)
                pairs.append((image_path, caption))
            else:
                print(f"Failed to process image: {img_src}")
        except Exception as e:
            print(f"Error processing image {img_src}: {e}")

    return pairs

def get_output_directory(html_path):
    """
    Given the path to an HTML file, return the path to the output directory.
    
    Args:
        html_path (str): The path to the HTML file.
    
    Returns:
        str: The path to the output directory.
    """
    if not os.path.isfile(html_path):
        raise ValueError("The provided HTML file path is not valid.")
    
    # Generate the output directory path based on the HTML file path
    output_directory = os.path.join(os.path.dirname(html_path), 'extracted_images')
    return output_directory



# Example usage with corrected paths
#html_path = input("Enter the path to the HTML: ").strip().strip('"')

# Example usage
html_path = ask_file("Select the HTML file:", filetypes=[("HTML files", "*.html")])
if not html_path:
    print("No file selected. Exiting.")
else:
    html_path = html_path.strip().strip('"')  # Remove extra whitespace or quotes
    print(f"HTML path entered: {html_path}")


output_directory = get_output_directory(html_path)

pairs = extract_images_and_captions(html_path, output_directory)
if pairs:
    for image_path, caption in pairs:
        print(f"Image: {image_path}, Caption: {caption}")
else:
    print("No images or captions were processed.")

# With JSON and ORB - My old Workflow

import os
from pathlib import Path
import cv2
import numpy as np


def preprocess_image(image_path, size=(300, 300)):
    """Load and preprocess the image for matching."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error reading image: {image_path}")
        return None
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, size)
    return resized_image

def compute_orb_matches(image1, image2):
    """Compute the ORB matches between two images."""
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def match_images_with_captions(folder1, folder2, captions):
    """Match images between two folders using ORB and associate captions."""
    images_folder1 = list(Path(folder1).glob('*.*'))
    images_folder2 = list(Path(folder2).glob('*.*'))
    
    if not images_folder1:
        print(f"No images found in folder1: {folder1}")
    if not images_folder2:
        print(f"No images found in folder2: {folder2}")
    
    matches = []
    for img1_path in images_folder1:
        img1_preprocessed = preprocess_image(str(img1_path))
        if img1_preprocessed is None:
            continue
        
        best_match = None
        best_match_count = -1
        
        for img2_path in images_folder2:
            img2_preprocessed = preprocess_image(str(img2_path))
            if img2_preprocessed is None:
                continue
            
            orb_matches = compute_orb_matches(img1_preprocessed, img2_preprocessed)
            match_count = len(orb_matches)
            
            if match_count > best_match_count:
                best_match_count = match_count
                best_match = img2_path
        
        if best_match:
            img1_filename = os.path.basename(img1_path)
            caption = captions.get(img1_filename, None)
            matches.append((img1_path, best_match, best_match_count, caption))
    
    return matches

def create_captions_mapping(pairs):
    """Create a dictionary mapping image filenames to captions."""
    captions = {}
    for image_path, caption in pairs:
        filename = os.path.basename(image_path)
        captions[filename] = caption
    return captions

def resize_to_common_height(img1, img2):
    """Resize images to have the same height."""
    height1, width1 = img1.shape[:2]
    height2, width2 = img2.shape[:2]
    
    common_height = min(height1, height2)
    new_width1 = int((common_height / height1) * width1)
    new_width2 = int((common_height / height2) * width2)
    
    img1_resized = cv2.resize(img1, (new_width1, common_height))
    img2_resized = cv2.resize(img2, (new_width2, common_height))
    
    return img1_resized, img2_resized

def visualize_matches_with_captions(matches):
    """Visualize the matched images with captions using OpenCV."""
    if not matches:
        print("No matches found.")
        return
    
    for img1_path, img2_path, match_count, caption in matches:
        img1 = cv2.imread(str(img1_path))
        img2 = cv2.imread(str(img2_path))
        
        if img1 is None or img2 is None:
            print(f"Error loading images: {img1_path} or {img2_path}")
            continue
        
        # No need to convert to RGB, keep it in BGR for proper display
        img1_resized, img2_resized = resize_to_common_height(img1, img2)
        
        combined_img = np.hstack((img1_resized, img2_resized))
        
        # Display the combined image
        cv2.imshow(f"Match Count: {match_count}\nCaption: {caption if caption else 'No caption'}", combined_img)
        
        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
folder1 = output_directory
#folder2 = input("Enter the path to the Folder with high res images: ").strip().strip('"')


# Example usage
folder2 = ask_directory("Select the Folder with High Res Images")
if not folder2:
    print("No folder selected. Exiting.")
else:
    print(f"Folder selected: {folder2}")
# Check if the input is not empty
if not folder2:
    print("No folder selected. Exiting.")
else:
    folder2 = folder2.strip().strip('"')




pairs = extract_images_and_captions(html_path, output_directory)
captions = create_captions_mapping(pairs)

matched_images = match_images_with_captions(output_directory, folder2, captions)
visualize_matches_with_captions(matched_images)


def create_mapping_from_matches(matches):
    """Create a dictionary mapping image filenames to captions based on matched images."""
    mapping = {}
    for img1_path, img2_path, score, caption in matches:
        # Use the filename from the Moula folder (img2_path)
        img2_filename = os.path.basename(img2_path)
        mapping[img2_filename] = caption if caption else "No caption"
    return mapping

# Example usage
# Assuming `matched_images` contains the matched results with captions
mapping_from_matches = create_mapping_from_matches(matched_images)

# Print or use the mapping as needed
for filename, caption in mapping_from_matches.items():
    print(f"{filename}: {caption}")

# Optional: Save the mapping to a file for later use
import json
mapping_file_path = r"C:\Users\User\Desktop\mapping_from_matches.json"
with open(mapping_file_path, 'w') as file:
    json.dump(mapping_from_matches, file, indent=4)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException

# Path to your ChromeDriver executable
CHROME_DRIVER_PATH = r'C:\Users\User\Desktop\iRonhack\Final Project\chromedriver-win64\chromedriver.exe'

# Load the captions mapping from a JSON file
mapping_file_path = r"C:\Users\User\Desktop\mapping_from_matches.json"
with open(mapping_file_path, 'r') as file:
    captions_dict = json.load(file)

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized
    driver_service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    return driver

def login_to_wordpress(driver, url, username, password):
    driver.get(url)
    time.sleep(5)  # Wait for the login page to load

    try:
        # Enter the username
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'usernameOrEmail'))
        )
        username_input.clear()  # Clear any existing text
        username_input.send_keys(username)

        # Click the "Continue" button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Continue")]'))
        )
        continue_button.click()

        # Wait for the password input field to be visible
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        password_input.clear()  # Clear any existing text
        password_input.send_keys(password)

        # Click the "Log In" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Log In")]'))
        )
        login_button.click()

        # Confirm login by checking the URL or some element on the dashboard
        WebDriverWait(driver, 10).until(
            EC.title_contains("Dashboard")
        )
        print("Login successful")

    except Exception as e:
        print(f"An error occurred during login: {e}")
        driver.quit()
        raise

def navigate_to_media_library(driver, base_url):
    media_library_url = f"{base_url}/wp-admin/upload.php?mode=list"
    driver.get(media_library_url)
    WebDriverWait(driver, 10).until(EC.title_contains("Media Library"))
    print("Navigated to media library in list mode")

def upload_image(driver, image_path, base_url):
    media_library_url1 = f"{base_url}/wp-admin/media-new.php?browser-uploader"
    driver.get(media_library_url1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id,'html5_')]"))
    ).send_keys(image_path)
    time.sleep(10)  # Adjust based on file size and network speed
    print(f"Uploaded image: {image_path}")

def add_caption(driver, caption_text, base_url):
    if caption_text == "No caption":
        print("No caption available for this image.")
        return  # Skip captioning if there's no caption
    
    try:
        navigate_to_media_library(driver, base_url)
        
        # Wait for the list of images to be visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wp-list-table")))
        
        # Wait for and click the most recent image (first row's image link)
        image_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".wp-list-table .title a"))
        )
        image_link.click()
        
        # Wait for the edit page to load and the caption field to be interactable
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'attachment_caption')))
        caption_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'attachment_caption'))
        )
        
        caption_input.clear()
        caption_input.send_keys(caption_text)
        
        # Scroll to the "Update" button to ensure it's in view
        update_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'publish'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", update_button)
        
        # Wait for any potential loading overlays to disappear
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".loading-overlay"))
        )
        
        # Click the "Update" button using JavaScript if normal clicking fails
        driver.execute_script("arguments[0].click();", update_button)
        
        print(f"Added caption: {caption_text}")
    except Exception as e:
        print(f"An error occurred while adding caption: {e}")

def extract_image_details(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'poststuff')))

    # Extract the details
    dimensions_text = driver.find_element(By.CSS_SELECTOR, '.misc-pub-dimensions strong').text
    width, height = dimensions_text.replace('×', 'x').split('x')  # '×' might be different based on locale
    
    name = driver.find_element(By.ID, 'title').get_attribute('value')
    caption = driver.find_element(By.ID, 'attachment_caption').text
    url = driver.find_element(By.ID, 'attachment_url').get_attribute('value')

    details = {
        'width': width.strip(),
        'height': height.strip(),
        'name': name,
        'caption': caption.strip(),
        'url': url.strip()
    }
    
    return details

def generate_caption(width, height, name, caption, url):
    caption_html = (
        f'[caption align="aligncenter" width="{width}"]'
        f'<img class="size-full wp-image" src="{url}" alt="{name.replace("-", " ")}" width="{width}" height="{height}" /> '
        f'{caption}[/caption]'
    )
    return caption_html

def process_images(driver, num_images_to_process):
    image_htmls = []    # List to store HTML strings

    # List to hold details of images
    image_details_list = []

    # Iterate over the specified number of images
    for i in range(1, num_images_to_process + 1):
        try:
            # Locate and click the image
            image = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'tbody#the-list tr:nth-child({i}) a'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", image)
            time.sleep(1)  # Ensure the element is in view
            image.click()

            # Extract details from the image
            image_details = extract_image_details(driver)
            image_details_list.append(image_details)
            
            # Go back to the media library
            driver.back()
            
            # Wait for media library page to load again
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'the-list'))
            )

        except Exception as e:
            print(f"An error occurred while processing image {i}: {e}")

    # Generate captions for each image
    for details in image_details_list:
        caption_html = generate_caption(details['width'], details['height'], details['name'], details['caption'], details['url'])
        image_htmls.append(caption_html)

    return image_htmls

driver = init_driver()
try:
    # User inputs
    # url = input("Enter the WordPress login URL: ").strip()
    # username = input("Enter your WordPress username: ").strip()
    # password = input("Enter your WordPress password: ").strip()
    # num_images_to_process = int(input("Enter the number of images to process: ").strip())



    url = ask_url("Enter the WordPress login URL:")
    if not url:
        print("No URL entered. Exiting.")
    else:
        url = url.strip()  # Remove extra whitespace
        print(f"URL entered: {url}")


    # Example usage for username input
    username = ask_username("Enter your WordPress username:")
    if not username:
        print("No username entered. Exiting.")
    else:
        username = username.strip()  # Remove extra whitespace
        print(f"Username entered: {username}")

   # Ask for the WordPress password (input is masked)
    password = ask_password("Enter your WordPress password:")
    if not password:
        print("No password entered. Exiting.")
    else:
        password = password.strip()  # Remove extra whitespace
        print(f"Password entered: {password}")

    # Ask for the number of images to process
   # Example usage for numeric input
    num_images_input = ask_numeric("Enter the number of images to process:")
    if not num_images_input:
        print("No number entered. Exiting.")
    else:
        try:
            num_images_to_process = int(num_images_input.strip())
            print(f"Number of images to process: {num_images_to_process}")
        except ValueError:
            print("Invalid number entered. Please enter a valid integer.")


    # Extract base URL
    base_url = "/".join(url.split("/")[:3])  # This gets the protocol and domain (e.g., https://yoursite.wordpress.com)

    # Login and navigate
    login_to_wordpress(driver, url, username, password)
    navigate_to_media_library(driver, base_url)

    # Iterate through images in the folder
    for image_filename in os.listdir(folder2):
        image_path = os.path.join(folder2, image_filename)

        # Extract the caption from the dictionary, if it exists
        caption_text = captions_dict.get(image_filename, "No caption")

        upload_image(driver, image_path, base_url)
        time.sleep(10)  # Ensure the image is fully uploaded

        add_caption(driver, caption_text, base_url)

    navigate_to_media_library(driver, base_url)

    # Process images and generate captions
    image_htmls = process_images(driver, num_images_to_process)

    # Display the resulting HTML strings
    print("Generated HTML captions for images:")
    for html in image_htmls:
        print(html)

finally:
    driver.quit()


import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog
from bs4 import BeautifulSoup
import re

def get_multiline_input():
    """
    Display a modern dialog with a multi-line text input area.
    
    Returns:
        str: The text entered by the user.
    """
    # Create the root window
    root = tk.Tk()
    root.title("Multi-line Input")
    root.geometry("400x300")  # Set a reasonable size for the dialog
    root.withdraw()  # Hide the root window

    # Create a new Toplevel window for input
    input_window = tk.Toplevel(root)
    input_window.title("Input")
    input_window.geometry("400x300")  # Set size for the input dialog

    # Create a frame to hold the widgets
    frame = tk.Frame(input_window, padx=10, pady=10)
    frame.pack(expand=True, fill='both')

    # Create a label for the input prompt
    label = tk.Label(frame, text="Please paste your text below:")
    label.pack(anchor='w')

    # Create a scrolled text widget for multi-line input
    input_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=10, width=50)
    input_text.pack(expand=True, fill='both')

    # Variable to store the user input
    user_input = tk.StringVar()

    # Create a submit button
    def on_submit():
        user_input.set(input_text.get("1.0", tk.END).strip())
        input_window.destroy()

    submit_button = tk.Button(frame, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    # Run the Tkinter event loop
    root.wait_window(input_window)

    return user_input.get()

# Use the function to get the user's input
pasted_text = get_multiline_input()

print("Original text:")
print(pasted_text)

# Removing Spans
pattern_with_content = r'<span style="font-weight: 400;">(.*?)<\/span>'
pattern_empty = r'<span style="font-weight: 400;"><\/span>'
pasted_text = re.sub(pattern_with_content, r'\1', pasted_text, flags=re.DOTALL)
pasted_text = re.sub(pattern_empty, '', pasted_text)

# Replace Space tag &nbsp; with BR
def replace_nbsp_with_br(html):
    return re.sub(r'&nbsp;', '<br>', html)

pasted_text = replace_nbsp_with_br(pasted_text)

# Opening Anchor Tags in New Window
def add_target_blank_to_anchors(html, base_domain):
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.find_all('a', href=True)
    for a in anchors:
        href = a['href']
        if not href.startswith(base_domain):
            a['target'] = '_blank'
            a['rel'] = 'noopener'
    return str(soup)

base_domain = 'https://geoblogportugal.wordpress.com/'
modified_text = add_target_blank_to_anchors(pasted_text, base_domain)

# Ensuring that H2 tags are BOLD
def ensure_strong_in_h2(html):
    soup = BeautifulSoup(html, 'html.parser')
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        if h2.find('b'):
            for b in h2.find_all('b'):
                strong_tag = soup.new_tag('strong')
                strong_tag.extend(b.contents)
                b.replace_with(strong_tag)
        if not h2.find('strong'):
            strong_tag = soup.new_tag('strong')
            strong_tag.extend(h2.contents)
            h2.clear()
            h2.append(strong_tag)
    return str(soup)

modified_text_bold = ensure_strong_in_h2(modified_text)

# Ensuring that H3 tags are BOLD
def ensure_strong_in_h3(html):
    soup = BeautifulSoup(html, 'html.parser')
    h3_tags = soup.find_all('h3')
    for h3 in h3_tags:
        if h3.find('b'):
            for b in h3.find_all('b'):
                strong_tag = soup.new_tag('strong')
                strong_tag.extend(b.contents)
                b.replace_with(strong_tag)
        if not h3.find('strong'):
            strong_tag = soup.new_tag('strong')
            strong_tag.extend(h3.contents)
            h3.clear()
            h3.append(strong_tag)
    return str(soup)

modified_text_bold = ensure_strong_in_h3(modified_text_bold)

# Add numbers to Headings
def replace_list_with_numbered_h2(html):
    soup = BeautifulSoup(html, 'html.parser')
    counter = 1
    for list_tag in soup.find_all(['ul', 'ol']):
        for li in list_tag.find_all('li', attrs={'aria-level': '1'}):
            h2_tag = li.find('h2')
            if h2_tag:
                if not h2_tag.find('strong'):
                    strong_tag = soup.new_tag('strong')
                    strong_tag.extend(h2_tag.contents)
                    h2_tag.clear()
                    h2_tag.append(strong_tag)
                strong_tag = h2_tag.find('strong')
                strong_tag.insert(0, f"{counter}. ")
                li.replace_with(h2_tag)
                counter += 1
        list_tag.unwrap()
    return str(soup)

modified_text_counter = replace_list_with_numbered_h2(modified_text_bold)

def replace_list_with_numbered_h3(html):
    soup = BeautifulSoup(html, 'html.parser')
    counter = 1
    list_items = soup.find_all('li', attrs={'aria-level': '1'})
    for li in list_items:
        h3_tag = li.find('h3')
        if h3_tag:
            for b_tag in h3_tag.find_all('b'):
                strong_tag = soup.new_tag('strong')
                strong_tag.extend(b_tag.contents)
                b_tag.replace_with(strong_tag)
            strong_tag = h3_tag.find('strong')
            if strong_tag:
                strong_tag.insert(0, f"{counter}. ")
            li.replace_with(h3_tag)
            counter += 1
    return str(soup)

modified_text_counter_h3 = replace_list_with_numbered_h3(modified_text_counter)

# Replace BR-TAG With Spaces
def replace_br_with_nbsp(html):
    return re.sub(r'<br\s*/?>', '&nbsp;', html, flags=re.IGNORECASE)

final = replace_br_with_nbsp(modified_text_counter_h3)
print("Final text:")
print(final)

# Adding Generated IMG HTMLs to the Main HTML
import pyperclip

def make_pattern(description_text):
    # Split the description text into words to handle HTML tags between words
    words = re.split(r'\s+', description_text)
    
    # Function to escape word and allow for HTML tags
    def escape_word(word):
        return re.escape(word) + r'(\s*<[^>]+>\s*)?'
    
    # Match the complete description text, allowing HTML tags between words
    pattern = r'\s*'.join(escape_word(word) for word in words)
    
    return pattern

def replace_text_with_html(text, image_htmls):
    patterns_used = []
    images_without_captions = []
    
    for image_html in image_htmls:
        # Check if it's an image with a caption
        description_match = re.search(r'<img[^>]+> (\w.*?)\[/caption\]', image_html, re.DOTALL)
        if description_match:
            description_text = description_match.group(1).strip()
            
            # Create a regex pattern that matches the entire description text
            pattern = make_pattern(description_text)
            
            # Add the pattern to a list for reporting
            patterns_used.append(pattern)
            
            # Replace the matched text with the full image_html
            text = re.sub(pattern, image_html, text, flags=re.IGNORECASE | re.DOTALL)
        else:
            # Check if it's an image without a caption
            no_caption_match = re.search(r'<img[^>]+>', image_html)
            if no_caption_match:
                images_without_captions.append(image_html)
    
    # Remove duplicates from the list of images without captions
    images_without_captions = list(set(images_without_captions))
    
    # Move images without captions to the beginning of the text
    for img in reversed(images_without_captions):
        text = img + '\n\n' + text
    
    return text, patterns_used

text = final

# Assuming image_htmls is defined elsewhere

result_text, patterns_used = replace_text_with_html(text, image_htmls)

def display_text_in_tkinter(text):
    # Create the root window
    root = tk.Tk()
    root.title("Result Text")

    # Create a scrolled text widget
    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
    text_widget.pack(expand=True, fill='both')

    # Insert the text into the widget
    text_widget.insert(tk.END, text)

    # Make the text widget read-only
    text_widget.config(state=tk.DISABLED)

    # Run the Tkinter event loop
    root.mainloop()



# Display the text
display_text_in_tkinter(result_text)
