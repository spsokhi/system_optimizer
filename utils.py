from win10toast import ToastNotifier
import speedtest

def show_notification(message, title="System Optimizer"):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)

def test_internet_speed(output_callback=print):
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    output_callback(f"Download Speed: {download_speed:.2f} Mbps")
    output_callback(f"Upload Speed: {upload_speed:.2f} Mbps")
    show_notification(f"Download: {download_speed:.2f} Mbps | Upload: {upload_speed:.2f} Mbps", "Internet Speed Test")
