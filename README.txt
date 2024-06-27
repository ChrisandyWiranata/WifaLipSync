README FROM US

0. Lip-Sync berbeda dengan Voice Synthesis (penjelasan lebih lanjut di video demo)
Link dari Video Demo:
https://drive.google.com/drive/folders/1SapbLMG2jvy1TvdwPkKOP_r_4MUXX_pg?usp=sharing

1. Pastikan folder project terletak di directory system C:

2. Pastikan telah menginstall ffmpeg, sudah kami sediakan di folder terpisah dengan WifaLipSync. Silahkan extract dan set variable environment terlebih dahulu, mohon mengikuti tutorial youtube sebagai referensi lebih lanjut (WAJIB); https://www.youtube.com/watch?v=DMEP82yrs5g. Lakukan instalasi dependency melalui pip install -r requirements.txt

3. Terdapat beberapa folder yang perlu diperhatikan, ada folder examples yang berisi dengan video-video hasil yang telah kami coba generate menggunakan aplikasi ini. Kemudian dilengkapi dengan folder sample yang berisi video dan audio mentah dari video yang di generate sebelumnya. Video dan audio sample tersebut bisa lansung digunakan untuk mencoba program.

4. Mohon perhatikan naming audio dan video yang akan kita gunakan untuk diupload dan digenerate menggunakan program, pastikan nama tidak memiliki spasi, seperti "Judul Audio.wav" (ini tidak bisa terbaca oleh program dan akan menghasilkan error), melainkan seperti "judulAudio.wav"

5. Program ini mengkonsumsi baterai yang lumayan tinggi, dan juga mengkonsumsi usage dari processor dan RAM. Sehingga disarankan untuk tidak multitasking ketika pengerjaan sedang berlansung

6. Dari hasil pantauan kami, berikut beberapa hal yg penting untuk diketahui bersama:

- Algoritma ini bekerja lebih baik terhadap video dengan resolusi rendah (360p dan 480p). Dan secara default, algoritma juga sudah mengubah video result yg di generate agar di compress ke 480p jika resolusi inputan 720p keatas. Namun yg terbaik adalah menggunakan video dengan resolusi rendah dari awal.

- Algoritma akan bekerja maksimal jika digunakan kepada video yg statis dalam pergerakan bibir, serta kepala dan mulut. Video dengan bibir yang mengarah vertikal lansung kedepan, serta tidak banyak pergerakan dari kepala dan mulut, akan memberikan hasil yang lebih baik.

- Untuk hasil yang paling natural gunakan audio dan video dengan durasi yang sama. Jika durasi video lebih panjang dari audio, maka hasil akan menyesuaikan sesuai dengan panjang audio dengan cara memotong otomatis durasi pada video sesuai dengan audio. Namun jika audio lebih panjang, maka akan terjadi pengulangan pada video setelah pemutaran awal habis.

7. Mohon untuk membaca kembali informasi yg tertera di aplikasi sebelum memulai menggunakan, serta lihat terlebih dahulu video demo yang diberikan. Terimakasih!
