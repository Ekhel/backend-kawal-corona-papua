# BACKEND LIVE DATA KASUS COVID 19 (PAPUA)

[![Build Status](https://travis-ci.com/Ekhel/backend-kawal-corona-papua.svg?branch=master)](https://travis-ci.com/Ekhel/backend-kawal-corona-papua)
[![Gitter](https://badges.gitter.im/jayapura_django/community.svg)](https://gitter.im/jayapura_django/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

![Flickr](https://live.staticflickr.com/65535/49699875306_d9f82bedca_k.jpg)

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

* Frontend :
  - [Kawal-Corona](https://github.com/Ekhel/kawal-corona)

* HOST
  - [Heroku](https://kawal-corona.herokuapp.com)

------------------------------------------------------------------------------

## Sumber WEB dan API :

* WEB :
  - [Kawal Corona](https://kawalcorona.com)
  - [Ethical Hacker Indonesia](https://hack.co.id)

* API Services :
  - [Data Indonesia : https://api.kawalcorona.com/indonesia](https://api.kawalcorona.com/indonesia)

    ```javascripts
    [
        {
          "name": "Indonesia",
          "positif": "514",
          "sembuh": "29",
          "meninggal": "48"
        }
    ]
    ```

  - [Data Provinsi : https://api.kawalcorona.com/indonesia/provinsi](https://api.kawalcorona.com/indonesia/provinsi)

    ```javascripts
    [
        {
            "attributes": {
              "FID": 11,
              "Kode_Provi": 31,
              "Provinsi": "DKI Jakarta",
              "Kasus_Posi": 307,
              "Kasus_Semb": 22,
              "Kasus_Meni": 29
            }
        }
    ]	
    ```

  - [Data Global Per Negara : https://api.kawalcorona.com/](https://api.kawalcorona.com/)

    ```javascripts
    [
        {
            "attributes": {
            "OBJECTID": 59,
            "Country_Region": "China",
            "Last_Update": 1584097775000,
            "Lat": 30.5928,
            "Long_": 114.3055,
            "Confirmed": 81346,
            "Deaths": 3265,
            "Recovered": 72355,
            "Active": 5726
            }
        }
    ]			
    ```
    
  - [Data Global Positif : https://api.kawalcorona.com/positif/](https://api.kawalcorona.com/positif)

    ```javascripts
    {
      "name": "Total Positif",
      "value": "307,278"
    }
    ```

  - [Data Global Meninggal : https://api.kawalcorona.com/meningggal/](https://api.kawalcorona.com/meniggal)

    ```javascripts
    {
      "name": "Total Meninggal",
      "value": "13,049"
    }
    ```
  - [Data Global Sembuh : https://api.kawalcorona.com/sembuh/](https://api.kawalcorona.com/sembuh)

    ```javascripts
    {
      "name": "Total Sembuh",
      "value": "92,373"
    }
    ```


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
    