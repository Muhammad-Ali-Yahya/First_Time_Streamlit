import streamlit as st
import pandas as pd
import datetime
#import matplotlib.pyplot as plt

st.title("🎈 My new app") #Ini merupakan function yang digunakan untuk menampilkan teks dalam format judul. Kode yang dapat Anda gunakan untuk menerapkan function tersebut adalah seperti di bawah ini.

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'c1': [1,2,3,4],
    'c2': [10, 20, 30,40],
}))

st.markdown(
     """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)     #Function ini digunakan untuk menampilkan output dari argument markdown. Berikut merupakan contoh kode untuk menggunakannya.

st.header('Pengembangan Dashboard') #Function ini digunakan untuk menampilkan output teks sebagai format header. Berikut contoh penulisan kode untuk menggunakannya.

st.subheader('Pengembangan Dashboard') #Ini merupakan function yang digunakan untuk menampilkan output teks sebagai format subheader.

st.caption('Copyright (c) 2023') #Function berikutnya ialah caption(). Ia merupakan function yang digunakan untuk menampilkan output teks dalam ukuran kecil. Function ini biasanya digunakan untuk menampilkan caption, footnotes, dll. Contoh penggunaannya seperti di bawah ini.

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python') 
#Pada beberapa case, kita harus menampilkan potongan kode ke dalam streamlit app (web app yang dibuat menggunakan streamlit). Untuk menjawab hal ini, streamlit telah menyediakan sebuah function bernama code(). Kode di bawah ini merupakan contoh penggunaan dari function tersebut.

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")#Function terakhir yang dapat digunakan untuk menampilkan elemen teks ialah latex(). Sesuai namanya, function tersebut digunakan untuk menampilkan mathematical expression yang ditulis dalam format LaTeX. Berikut contoh kode untuk menggunakan function latex().

st.text('Halo, calon praktisi data masa depan.')#Function selanjutnya ialah text(). Function ini digunakan untuk menampilkan sebuah normal teks. Berikut merupakan contoh kode untuk mengguankannya.

#Data Display

#1.dataframe()
#Function pertama yang bisa kita gunakan untuk menampilkan data ke dalam streamlit app ialah dataframe(). Ia merupakan function yang digunakan untuk menampilkan DataFrame sebagai sebuah tabel interaktif. Pada function ini, kita bisa mengatur ukuran dari table yang ingin ditampilkan menggunakan parameter width dan height. Berikut merupakan contoh kode untuk menampilkan data menggunakan function dataframe().

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

#2.table()
#Selain dataframe(), kita juga bisa menggunakan function table()untuk menampilkan data ke dalam streamlit app. Ia dapat digunakan untuk menampilkan data dalam bentuk static table. Berikut merupakan contoh penggunaannya.

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

#3.metric()
#Ketika membuat dashboard, terkadang kita perlu menampilkan sebuah metrik tertentu. Untuk melakukan hal ini, kita bisa memanfaatkan function metric(). Function ini dapat membantu kita untuk menampilkan sebuah metrik tertentu beserta detailnya seperti label, value serta besar perubahan nilainya. Berikut merupakan contoh kode untuk menggunakannya.

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

#4.json()
#Selain bentuk DataFrame atau tabel, terkadang kita juga perlu menampilkan data dalam format JSON. Streamlit telah menyediakan function json() untuk menampilkan data dalam format JSON. Berikut merupakan contoh penggunaannya.

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

#4.Chart
#Basic element terakhir yang perlu kita ketahui ialah chart. Sesuai namanya, elemen ini dapat digunakan untuk menampilkan grafik visualisasi data ke dalam streamlit app. Elemen inilah yang akan sering kita gunakan untuk membuat dashboard nantinya. Sebenarnya streamlit telah menyediakan banyak sekali function untuk mendukung berbagai library visualisasi data (dokumentasi: chart). Namun, pada materi ini, kita hanya akan fokus pada function pyplot().

#Function pyplot() dapat digunakan untuk menampilkan grafik visualisasi data yang dibuat menggunakan matplotlib. Berikut merupakan contoh kode untuk menggunakannya.

### x = np.random.normal(15, 5, 250)fig, ax = plt.subplots()ax.hist(x=x, bins=15)st.pyplot(fig) ###


#Basic Widgets dalam Streamlit

#Input Widget

#1.Text input
#Text input merupakan widget yang digunakan untuk memperoleh inputan berupa single-line text. Kita bisa menggunakan function text_input() untuk membuat widget ini. Berikut merupakan contoh kode untuk membuatnya.

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama', name)

#2. Text-area
#Text area merupakan widget yang memungkinkan pengguna untuk menginput multi-line text. Untuk membuat widget ini, streamlit telah menyediakan function bernama text_area(). Kode di bawah ini merupakan contoh kode untuk menggunakan function tersebut.

text = st.text_area('Feedback')
st.write('Feedback: ', text)

#Number input
#Widget berikutnya yang akan kita bahas ialah number input . Ia merupakan widget yang digunakan untuk memperoleh inputan berupa angka dari pengguna. Anda dapat menggunakan contoh kode berikut untuk membuat number input widget menggunakan function number_input().

number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

#Data Input
#Selain inputan berupa angka dan teks, pada beberapa kasus kita juga membutuhkan input berupa tanggal dari pengguna melalui date input widget. Kita dapat membuat widget tersebut menggunakan function date_input(). Berikut merupakan contoh kode untuk menggunakannya.

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

#File uploader
#Widget selanjutnya yang akan kita bahas ialah file uploader. Widget ini memungkinkan kita meminta pengguna untuk meng-upload sebuah berkas tertentu ke dalam web app. Kita dapat membuat file uploader widget menggunakan function file_uploader() seperti pada contoh kode berikut. 

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

#Camera Input
#Selain file uploader, streamlit juga menyediakan camera input widget yang dapat digunakan untuk meminta user mengambil gambar melalui webcam sekaligus mengunggahnya.  Hal ini tentunya dilakukan dengan persetujuan pengguna. Berikut merupakan contoh kode untuk membuat camera input widget menggunakan function camera_input().

picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


#Button Widgets 
#Oke, kategori widget selanjutnya yang akan kita bahas ialah button widget. Ia merupakan kategori widget yang terdiri dari button, checkbox, radio button, dll

#Button
#Button merupakan widget untuk menampilkan tombol interaktif. Tombol tersebut dapat digunakan pengguna untuk melakukan aksi tertentu. Untuk membuat widget ini, kita bisa menggunakan function button() seperti contoh berikut.
if st.button('Say hello'):
    st.write('Hello there')

#Checkbox
#Checkbox merupakan widget yang digunakan untuk menampilkan sebuah checklist untuk pengguna. Kita bisa menggunakan function checkbox() untuk membuat dan menampilkan checklist dalam streamlit app. Berikut contoh kode untuk melakukannya.

agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

#Radio button
#Selain button dan checkbox, terkadang kita juga membutuhkan radio button untuk menghasilkan web app yang interaktif. Ia merupakan widget yang memungkinkan pengguna untuk memilih satu dari beberapa pilihan yang ada. Untuk membuat widget ini, kita bisa menggunakan function radio() seperti pada contoh kode berikut.

genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

#Select Box
#Select box merupakan widget yang memungkinkan pengguna untuk memilih salah satu dari beberapa pilihan yang ada. Ia merupakan opsi alternatif dari radio button. Streamlit telah menyediakan function selectbox() untuk membuat select box widget. Berikut contoh penggunaannya.

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

#Multiselect
#Widget lain yang harus kita ketahui ialah multiselect. Ia merupakan widget yang digunakan agar user dapat memilih lebih dari satu pilihan dari sekumpulan pilihan yang ada. Untuk mempermudah kita dalam membuat multiselect widget, streamlit telah menyediakan function bernama multiselect(). Berikut contoh kode untuk menggunakan function tersebut.

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

#Slider
#Slider merupakan widget yang memungkinkan pengguna untuk untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan. Streamlit telah menyediakan function slider() untuk membuat slider widget. Berikut merupakan contoh penggunaannya.

#values = st.slider(
#    label='Select a range of values',
 #   min_value=0, max_value=100, value=(0, 100))
# st.write('Values:', values)


#Basic Layouts dalam Streamlit
#Untuk membuat dashboard yang rapi, kita perlu belajar cara mengatur layout atau tampilan dari sebuah dashboard. Nah, pada materi kali ini, kita akan mengupas tuntas tentang basic layout dalam streamlit. 

#Sebagai sebuah web app framework, streamlit telah menyediakan berbagai pilihan layout yang dapat digunakan untuk mengatur tampilan web app (atau dashboard) yang akan dibuat. Pilihan layout yang tersedia antara lain sidebar, columns, tabs, expander, serta container. Tentunya setiap pilihan layout tersebut memiliki fungsi dan kegunaannya masing-masing. Yuk, kita bahas satu per satu! 

#sidebar
#Elemen layout pertama yang akan kita bahas ialah sidebar. Ia merupakan area yang berada di samping konten utama. Pada streamlit, posisi sidebar secara default berada di bagian kiri dari konten utama dan dapat memuat berbagai hal mulai dari gambar, teks, hingga widget.    

#Untuk menambahkan sebuah elemen atau widget ke dalam sidebar, kita bisa menggunakan notasi with yang diikuti sebuah object bernama sidebar yang telah disediakan oleh streamlit. Berikut merupakan contoh kode untuk menambah sebuah elemen dan widget ke dalam sidebar.

st.title('Belajar Analisa Data')

with st.sidebar:
    
    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='Select a range of values', 
        min_value=0, max_value=100, value=(0, 100)
    )
    
    st.write('Values', values)

#Columns
#Columns merupakan elemen layout yang memungkinkan kita untuk mengatur tampilan pada konten utama ke dalam beberapa kolom sesuai kebutuhan. Gambar berikut merupakan ilustrasi tampilan dari elemen layout ini. 

#Untuk membuat column dalam streamlit app, kita harus membuat object dari setiap kolom terlebih dahulu. Hal ini dapat dilakukan dengan memanfaatkan function columns(). Selanjutnya, kita hanya perlu menambahkan sebuah elemen atau widget ke dalam column tersebut menggunakan notasi with. Berikut merupakan contoh kode untuk membuat column dalam streamlit.

st.title('Belajar Analisis Data')
col1, col2, col3 = st.columns(3)
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

#Sebenarnya, kita bisa dengan bebas mengatur ukuran dari column yang dibuat. Nah, untuk melakukan hal ini, kita harus memasukkan sebuah list yang berisi perbandingan ukuran dari kolom yang akan dibuat. Sebagai contoh, kode di bawah ini akan menampilkan 3 buah kolom  dengan perbandingan 2:1:1.

st.title('Belajar Analisis Data')
col1, col2, col3 = st.columns([2, 1, 1])
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

#tabs
#Elemen layout berikutnya yang terdapat dalam streamlit ialah tabs. Ia merupakan elemen layout yang memungkinkan kita untuk menambahkan beberapa tabs ke dalam konten utama. Hal ini tentunya akan sangat membantu kita dalam menghasilkan dashboard yang interaktif. 

#Sama halnya dengan columns yang sebelumnya kita bahas, untuk membuat tabs, kita harus membuat object dari setiap tab menggunakan function tabs() yang diikuti dengan list dari nama dari setiap tab. Berikut contoh kode untuk membuat tabs dalam streamlit app.

st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

#Container
#Container merupakan elemen layout dalam streamlit yang memungkinkan kita untuk membuat sebuah wadah untuk menampung suatu atau beberapa elemen dengan ukuran yang tetap. Container ini dapat kita gunakan untuk menghasilkan dashboard yang rapi.

#Untuk membuat container, kita bisa menggunakan notasi with dan diikuti function container(). Kode di bawah ini merupakan contoh kode untuk membuat container dalam streamlit app. 

#import matplotlib as plt
#import numpy as np

#with st.container():
    #st.write("Inside the container")
    
    #x = np.random.normal(15, 5, 250)
 
    #fig, ax = plt.subplots()
    #ax.hist(x=x, bins=15)
   # st.pyplot(fig) 
 
#st.write("Outside the container")

#Expander
#Elemen layout selanjutnya yang tidak kalah penting ialah expander. Anda dapat menganggap elemen layout ini sebagai sebuah container yang dapat diperluas atau diciutkan secara interaktif.

#Untuk membuat elemen layout ini, kita bisa menggunakan notasi with dan diikuti dengan function expander() seperti pada contoh kode berikut.

#import streamlit as st
#import matplotlib.pyplot as plt
#import numpy as np
 
#x = np.random.normal(15, 5, 250)
 
#fig, ax = plt.subplots()
#ax.hist(x=x, bins=15)
#st.pyplot(fig) 
 
#with st.expander("See explanation"):
    #st.write(
        #"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        #sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        #Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        #nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        #in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        #nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        #sunt in culpa qui officia deserunt mollit anim id est laborum.
        #"""
    #)