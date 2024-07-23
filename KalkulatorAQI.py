import streamlit as st
import requests
from streamlit_lottie import st_lottie  

# file json format (File path)
lottie_url = "https://lottie.host/014c7f55-c04a-4e92-b604-4c4899e3a5e9/x2n7xRzfEB.json"
        
# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
        
        

# Fungsi untuk menghitung AQI berdasarkan PM2.5
def calculate_aqi(pm25):
    c = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
    i = [0, 50, 100, 150, 200, 300, 400, 500]

    # Menghitung nilai IAQI (Individual AQI) untuk PM2.5
    if pm25 <= c[1]:
        aqi = ((i[1] - i[0]) / (c[1] - c[0])) * (pm25 - c[0]) + i[0]
    elif pm25 <= c[2]:
        aqi = ((i[2] - i[1]) / (c[2] - c[1])) * (pm25 - c[1]) + i[1]
    elif pm25 <= c[3]:
        aqi = ((i[3] - i[2]) / (c[3] - c[2])) * (pm25 - c[2]) + i[2]
    elif pm25 <= c[4]:
        aqi = ((i[4] - i[3]) / (c[4] - c[3])) * (pm25 - c[3]) + i[3]
    elif pm25 <= c[5]:
        aqi = ((i[5] - i[4]) / (c[5] - c[4])) * (pm25 - c[4]) + i[4]
    elif pm25 <= c[6]:
        aqi = ((i[6] - i[5]) / (c[6] - c[5])) * (pm25 - c[5]) + i[5]
    elif pm25 <= c[7]:
        aqi = ((i[7] - i[6]) / (c[7] - c[6])) * (pm25 - c[6]) + i[6]
    else:
        aqi = 500

    return round(aqi)

# Fungsi untuk mendapatkan deskripsi kualitas udara berdasarkan nilai AQI
def get_aqi_description(aqi_value):
    if aqi_value <= 50:
        return "Kualitas udara baik; tidak ada atau sedikit risiko bagi kesehatan."
    elif aqi_value <= 100:
        return "Kualitas udara sedang; risiko kesehatan bagi kelompok sensitif."
    elif aqi_value <= 150:
        return "Kualitas udara tidak sehat bagi kelompok sensitif."
    elif aqi_value <= 200:
        return "Kualitas udara tidak sehat; bagi semua orang dapat terpengaruh."
    elif aqi_value <= 300:
        return "Kualitas udara sangat tidak sehat; efek serius pada kesehatan."
    else:
        return "Kualitas udara berbahaya; risiko kesehatan darurat."

# Fungsi untuk mendapatkan warna berdasarkan nilai AQI
def get_aqi_color(aqi_value):
    if aqi_value <= 50:
        return "green"  # warna untuk AQI baik
    elif aqi_value <= 100:
        return "yellow"  # warna untuk AQI sedang
    elif aqi_value <= 150:
        return "orange"  # warna untuk AQI tidak sehat
    elif aqi_value <= 200:
        return "red"  # warna untuk AQI sangat tidak sehat
    else:
        return "purple"  # warna untuk AQI berbahaya

# Fungsi untuk menampilkan UI aplikasi menggunakan Streamlit
def main():
    # List of options for the radio button
    options = ('Home', 'Kalkulator AQI')
    
    # Display a radio button in the sidebar
    selected_option = st.sidebar.selectbox('Main Menu', options)
    
# Perform actions based on the selected option
    if selected_option == 'Home':
            # Pembuatan 2 kolom
        col1, col2 = st.columns([1, 2])

        with col1 :
                st.header ("Project LPK Kelompok 10")

                st.write ("1. Aura Shyfa (2330490)")
                st.write ("2. Nasywa Rahmadani H (2330518)")
                st.write ("3. Nazmi Asyam (2330519)")
                st.write ("4. Shafiqah Fauziah (2330530)")
                st.write ("5. Selviana Valia (2230471)")
                st.write ("6. Zaki Raditya (2330534)")

            
        # Memproses animasi lottie
        lottie_json = load_lottie_url(lottie_url)
            
        # Menampilkan animasi lottie
        with col2 :
            if lottie_json is not None:
                st_lottie(lottie_json)
            else:
                st.write("Failed to load Lottie animation.")
                
    elif selected_option == 'Kalkulator AQI':
        st.title('Kalkulator AQI (Air Quality Index)')
        st.write('Masukkan nilai PM2.5 untuk menghitung AQI:')
    
        pm25_input = st.number_input('PM2.5 (µg/m³)', min_value=0.0, step=0.1, format='%f')
    
        if st.button('Hitung AQI'):
            if pm25_input:
                aqi_value = calculate_aqi(pm25_input)
                aqi_description = get_aqi_description(aqi_value)
                aqi_color = get_aqi_color(aqi_value)
    
                st.subheader(f'Nilai AQI yang dihitung adalah: {aqi_value}')
                st.markdown(f'<p style="color: {aqi_color}; font-size: large;">{aqi_description}</p>', unsafe_allow_html=True)
    
                # Menampilkan informasi tambahan berdasarkan rentang nilai AQI
                st.subheader('Kondisi berdasarkan nilai AQI:')
                if aqi_value <= 50:
                    st.markdown("Kualitas udara baik; tidak ada atau sedikit risiko bagi kesehatan.")
                elif aqi_value <= 100:
                    st.markdown("Kualitas udara sedang; risiko kesehatan bagi kelompok sensitif.")
                elif aqi_value <= 150:
                    st.markdown("Kualitas udara tidak sehat bagi kelompok sensitif.")
                elif aqi_value <= 200:
                    st.markdown("Kualitas udara tidak sehat; bagi semua orang dapat terpengaruh.")
                elif aqi_value <= 300:
                    st.markdown("Kualitas udara sangat tidak sehat; efek serius pada kesehatan.")
                else:
                    st.markdown("Kualitas udara berbahaya; risiko kesehatan darurat.")
                    
                st.image("imgweb/aqi.png", use_column_width=True)
                    
if __name__ == '__main__':
    main()
