<h3 align="center">
<strong>BACKEND LIVE DATA KASUS COVID 19 (PAPUA)</strong>
</h3>

![Flickr](https://live.staticflickr.com/65535/49699875306_d9f82bedca_k.jpg)
<p align="center">
  <a href="https://travis-ci.com/Ekhel/backend-kawal-corona-papua"><img src="https://travis-ci.com/Ekhel/backend-kawal-corona-papua.svg?branch=master" alt="Build Status"></a>
  <a href="https://gitter.im/jayapura_django/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge"><img src="https://badges.gitter.im/jayapura_django/community.svg" alt="Gitter"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>

</p>

## System Requirements :
* Language :
  - Python

* Framework :
  - Django 2.2.8

* DBMS :
  - SQLite (On Local)
  - Postgre (On Heroku)

* Library :
  - Django REST Framework (API)
  - Gunicorn (Web Server)
  - WhiteNoise (Static Files)
  - Django CORS-Header (Middleware Cors Origin)

* Frontend :
  - [Kawal-Corona](https://github.com/Ekhel/kawal-corona)

* HOST
  - [Heroku Cloud](https://heroku.com)

------------------------------------------------------------------------------

## Sumber WEB dan API :

* WEB :
  - [Kawal Corona Indonesia](https://kawalcorona.com)
  - [Ethical Hacker Indonesia](https://hack.co.id)
  - [Kawal Corona Papua](https://kawal-corona.herokuapp.com)


* API Services :
  - [Data Indonesia : https://api.kawalcorona.com/indonesia](https://api.kawalcorona.com/indonesia)

  - [Data Provinsi : https://api.kawalcorona.com/indonesia/provinsi](https://api.kawalcorona.com/indonesia/provinsi)

  - [Data Global Per Negara : https://api.kawalcorona.com/](https://api.kawalcorona.com/) 

  - [Data Global Positif : https://api.kawalcorona.com/positif/](https://api.kawalcorona.com/positif)

  - [Data Global Meninggal : https://api.kawalcorona.com/meningggal/](https://api.kawalcorona.com/meniggal)
  
  - [Data Global Sembuh : https://api.kawalcorona.com/sembuh/](https://api.kawalcorona.com/sembuh)


* Backend API (Data Khusus Provinsi Papua)
  - [API ROOT](https://kawal-corona.herokuapp.com/api/)
  - [API Kabupaten](https://kawal-corona.herokuapp.com/api/kabupeten/)
  
    ```javascripts
    {
      "count": 23,
      "next": "https://kawal-corona.herokuapp.com/api/kabupaten/?page=2",
      "previous": null,
      "results": [
        {
          "id_kabupaten": 1,
          "nama": "Jayapura Kota",
          "lon": "-",
          "lat": "-"
        }
      ] 
    }
    ```

  - [API Personal Positif](https://kawal-corona.herokuapp.com/api/penderita/)

    ```javascripts
    {
      "count": 3,
      "next": "null",
      "previous": null,
      "results": [
        {
          "id_penderita": 1,
          "nama_lengkap": "-----",
          "lokasi": 8,
          "gender": "perempuan",
          "status": "perawatan"
        },
      ] 
    }
    ```

  - [API Rumah Sakit Rujukan](https://kawal-corona.herokuapp.com/api/rumahsakit/)

    ```javascripts
    {
      "count": 1,
      "next": "null",
      "previous": null,
      "results": [
        {
            "id_rs": 1,
            "rumah_sakit": "RSUD JAYAPURA",
            "lokasi": "Jayapura Kota",
            "lat": "-",
            "lon": "-"
        },
      ]
    }
    ```

  - [API Informasi](https://kawal-corona.herokuapp.com/api/informasi/)
  - [API Papan Informasi](https://kawal-corona.herokuapp.com/api/papaninfo/)

    ```javascripts
    {
      "count": 1,
      "next": "null",
      "previous": null,
      "results": [
        {
            "id_item": 1,
            "tanggal": "2020-04-04",
            "odp": "6723",
            "pdp": "44",
            "positif": "18",
            "sembuh": "3",
            "meninggal": "1"
        }
      ]
    }
    ```
-------------------------------------------------------------------------------------------------------------

## Halaman Yang Tersedia :
  - [x] Dashboard
  - [x] CRUD Kabupaten
  - [x] CRUD Pasien Positif
  - [x] CRUD Rumah Sakit Rujukan
  - [x] CRUD Informasi harian Kasus Covid 19 Prov Papua (Papan Informasi)


## Screen :
  - ![positif](https://live.staticflickr.com/65535/49737626967_26cb3de065_z.jpg)
  -----------------------------------------------------------------------------------------------------------
  - ![dashboard](https://live.staticflickr.com/65535/49737294806_ab96efe58c_z.jpg)

-------------------------------------------------------------------------------------------------------------

## Kontribusi Data :
  - Saya Belum Memiliki Sumber Data yang benar" valid.
  - Sebagian Data Kasus di Provinsi Papua yang ada pada database backend diambil dari 60% Hasil Tracking Media.
  - Jika teman" ingin Berkontribusi terkait data dengan sangat senang hati saya akan menerima.
  - email saya terkait Data : **michaekarafir@gmail.com**
  - Atau bisa chat pada gitter klik pada badge gitter diatas, **chat on gitter**
  - Project ini Open Source siapa saja boleh untuk Berkontribusi Termasuk Data dan Repository.
  - Saran dan Masukan Sangat Saya butuhkan.

  Salam Sehat
  Michael.
    