import os
import subprocess
import sys
import win32com.client

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"📦 Chưa có `{package}`, đang cài đặt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Cài xong `{package}`")

install_and_import("win32com.client")

def convert_all_sldprt_to_step_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".sldprt") and not f.startswith("~$")]
    if not files:
        print("⚠️ Không có file .SLDPRT nào trong thư mục.")
        return

    swApp = win32com.client.Dispatch("SldWorks.Application")
    swApp.Visible = True

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        file_path = str(file_path)  # Đảm bảo truyền dạng chuỗi chuẩn COM

        print(f"➡️ Đang xử lý: {file_name}")

        try:
            model = swApp.OpenDoc(file_path, 1)  # 1 = Part
        except Exception as e:
            print(f"⚠️ Không mở được bằng OpenDoc, thử lại bằng OpenDoc6: {e}")
            try:
                model = swApp.OpenDoc6(file_path, 1, 0, "", 0, 0)
            except Exception as e2:
                print(f"❌ Lỗi mở file {file_name} bằng OpenDoc6: {e2}")
                continue

        if not model:
            print(f"❌ Không thể mở: {file_name}")
            continue

        step_path = os.path.join(folder_path, file_name.replace(".sldprt", ".step"))

        try:
            status = model.Extension.SaveAs(step_path, 0, 1, None, 0, 0)
            if status:
                print(f"✅ Đã chuyển: {step_path}")
            else:
                print(f"❌ Lỗi khi chuyển: {file_name}")
        except Exception as e:
            print(f"❌ Lỗi khi export STEP: {e}")

        swApp.CloseDoc(model.GetTitle())

    print("🎉 Hoàn tất chuyển đổi.")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📂 Đang chạy trong thư mục: {current_dir}")
    convert_all_sldprt_to_step_in_folder(current_dir)
