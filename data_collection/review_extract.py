from dotenv import load_dotenv
load_dotenv()
import serpapi
import os
import config as con
import pandas as pd
import csv


reviews = []  
topics = []  
place_id = []

fn=f'meta_csv/{con.search}_combined_output.csv'
cn='place_id'



with open(fn, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over rows in the CSV
    for row in csv_reader:
        # Access the column by its header (column name)
        # print(row[cn])
        place_id.append(row[cn])


        #serp API code will replace below result
        result = {
            "search_metadata": {
                "id": "66e416e67ebde5ae04e21976",
                "status": "Success",
                "json_endpoint": "https://serpapi.com/searches/a6486141832fc337/66e416e67ebde5ae04e21976.json",
                "created_at": "2024-09-13 10:41:42 UTC",
                "processed_at": "2024-09-13 10:41:42 UTC",
                "google_maps_reviews_url": "https://www.google.com/maps/place/data=!4m7!3m6!1s0x3bc2c07a37459ce3:0x90646f988cfb5dd9!5m2!4m1!1i2!9m1!1b1?hl=en&gl=",
                "raw_html_file": "https://serpapi.com/searches/a6486141832fc337/66e416e67ebde5ae04e21976.html",
                "prettify_html_file": "https://serpapi.com/searches/a6486141832fc337/66e416e67ebde5ae04e21976.prettify",
                "total_time_taken": 1.94
            },
            "search_parameters": {
                "engine": "google_maps_reviews",
                "place_id": "ChIJ45xFN3rAwjsR2V37jJhvZJA",
                "hl": "en"
            },
            "place_info": {
                "title": "Shri Omkareshwar Temple, Pune",
                "address": "Balgandharva Bridge, 233 Near, Chandrashekhar Govind Aapte Rd, Shaniwar Peth, Pune, Maharashtra 411030, India",
                "rating": 4.7,
                "reviews": 5569,
                "type": "Hindu temple"
            },
            "topics": [
                {
                    "keyword": "meditation",
                    "mentions": 111,
                    "id": "/m/0517l"
                },
                {
                    "keyword": "peshwa",
                    "mentions": 98,
                    "id": "/m/02zf5w"
                },
                {
                    "keyword": "architecture",
                    "mentions": 56,
                    "id": "/m/03nfmq"
                },
                {
                    "keyword": "river",
                    "mentions": 45,
                    "id": "/m/06cnp"
                },
                {
                    "keyword": "ancient",
                    "mentions": 39,
                    "id": "/m/0djmp"
                },
                {
                    "keyword": "bank",
                    "mentions": 35,
                    "id": "/m/017ql"
                },
                {
                    "keyword": "chimaji appa",
                    "mentions": 25,
                    "id": "/m/0czf9d"
                },
                {
                    "keyword": "mahashivratri",
                    "mentions": 22,
                    "id": "/m/044987"
                },
                {
                    "keyword": "18th century",
                    "mentions": 17,
                    "id": "/m/08b33"
                },
                {
                    "keyword": "om namah shivay",
                    "mentions": 17,
                    "id": "/m/04cg9t"
                }
            ],
            "reviews": [
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUNIbk1TS2Z3EAE!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgICHnMSKfw%7CCgsIlufVtgYQ4NaLCw%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "a week ago",
                    "iso_date": "2024-09-02T08:13:10Z",
                    "iso_date_of_last_edit": "2024-09-02T08:13:10Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipNXoRvjIsHSWAQRDMd0EhEEG65Vbg8JchK-NbO2=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPxI0A9gwEyw0DgM0fn9IjGohb0OBKwuu5-72kQ=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMGrtsy43MaHu7IL3k7MvDq7ql2tFFdczcqRBxg=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMeLhQmwzXjY-zp5ZqA0jNqahT2TPIe7N0DEIBp=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChZDSUhNMG9nS0VJQ0FnSUNIbk1TS2Z3EAE",
                    "user": {
                        "name": "Shekhar Ghuge",
                        "link": "https://www.google.com/maps/contrib/102552096805064651076?hl=en-US",
                        "contributor_id": "102552096805064651076",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjWGdQkGR4ZcL2r9BGW-wthxx0mnAH7HRPpZGBx63KPZWGsrtQVP=s120-c-rp-mo-ba4-br100",
                        "local_guide": True,
                        "reviews": 26,
                        "photos": 92
                    },
                    "snippet": "Stone temple besides river Mutha\nOmkareshwar Mandir is a 18th century temple buiilt by Chimaji appa, brother of Peshwa Bajirao I.\nThis temple is legacy & heritage of Pune, must visit by tourists.\nThis temple is very close to river and central place. It is quite big shiva temple built by Peshwa and maintained neatly. It is quite calm place even though it is in city. They celebrate festivals like Mahashivratri, Dasara in big way. Just opposite this temples, small ghat is available where last rituals are performed after deaths.",
                    "extracted_snippet": {
                        "original": "Stone temple besides river Mutha\nOmkareshwar Mandir is a 18th century temple buiilt by Chimaji appa, brother of Peshwa Bajirao I.\nThis temple is legacy & heritage of Pune, must visit by tourists.\nThis temple is very close to river and central place. It is quite big shiva temple built by Peshwa and maintained neatly. It is quite calm place even though it is in city. They celebrate festivals like Mahashivratri, Dasara in big way. Just opposite this temples, small ghat is available where last rituals are performed after deaths."
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSURydDkyQ29RRRAB!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgIDrt92CoQE%7CCgwIjor9tAYQuKi9xQI%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "a month ago",
                    "iso_date": "2024-07-21T05:03:17Z",
                    "iso_date_of_last_edit": "2024-07-23T05:52:14Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipPAsjurT5UA1ICOh9pr2FHeOw0oVX79kxh9VUMG=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNG8913M988g7kfSTWoLQ1_CA7qW4Bq7gYYjI5P=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPA7A1hFZSWsSP2FX1AkzLIwow5ZlWIXVu41fTP=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipM0UUs534vsjFraQBHXFJV2zmGjuWDeyp4TTS2p=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChdDSUhNMG9nS0VJQ0FnSURydDkyQ29RRRAB",
                    "user": {
                        "name": "RAP",
                        "link": "https://www.google.com/maps/contrib/102765868144964034372?hl=en-US",
                        "contributor_id": "102765868144964034372",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjU2FigpPWi-l3hw-Xbn4aGJmLeK4QvE9fv_2Cp0JqtJh2c48-Ov=s120-c-rp-mo-ba5-br100",
                        "local_guide": True,
                        "reviews": 298,
                        "photos": 835
                    },
                    "snippet": "Visiting Shree Omkareshwar Temple is not only a religious experience but also a cultural journey that connects you with Pune's rich heritage and spiritual traditions. Overall, Shree Omkareshwar Temple in Pune is a must-visit for anyone interested in architecture, spirituality, or simply seeking a peaceful escape from the city's hustle and bustle.",
                    "extracted_snippet": {
                        "original": "Visiting Shree Omkareshwar Temple is not only a religious experience but also a cultural journey that connects you with Pune's rich heritage and spiritual traditions. Overall, Shree Omkareshwar Temple in Pune is a must-visit for anyone interested in architecture, spirituality, or simply seeking a peaceful escape from the city's hustle and bustle."
                    },
                    "details": {
                        "visited_on": "Weekend",
                        "wait_time": "No wait"
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUNMcTd2RlpREAE!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgICLq7vFZQ%7CCgwInY7fswYQ4Lj74AI%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "2 months ago",
                    "iso_date": "2024-06-23T06:56:29Z",
                    "iso_date_of_last_edit": "2024-06-23T06:56:29Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipMv7EnRSDeEbbv-8rnI0vRYLD83ctoCbXOJnXeJ=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPgVRj9YpjRCh6vFtPDaKMMgR86BQS-_xI4KDAt=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOxMLj3zI981YznRDgK91ADiYky5PI4aXhLaUic=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMcWV9Q1uGxEnKv84Pfwu3ipWe9-e4ukEwyiGFp=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipONbzNpaWgG3sbT0daXiWFN77B0Uu6Brate3CAE=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChZDSUhNMG9nS0VJQ0FnSUNMcTd2RlpREAE",
                    "user": {
                        "name": "Divyesh Wadke",
                        "link": "https://www.google.com/maps/contrib/105910147993498483293?hl=en-US",
                        "contributor_id": "105910147993498483293",
                        "thumbnail": "https://lh3.googleusercontent.com/a/ACg8ocLXmB35cbRjNofDwLYgHIm-vQJXVFD7ZS160WoDkK6DRlf9mA=s120-c-rp-mo-ba6-br100",
                        "local_guide": True,
                        "reviews": 337,
                        "photos": 1707
                    },
                    "snippet": "Very beautiful Shiv mandir in the middle of hustle bustle of Pune city. The premises is very big, its difficult to imagine there is such big temple in densely packed area of Pune.\n\nThe temple is maintained very well. Premises are very clean and neat. Apart from the main Shiv mandir, there are a number of other small temples of other deities.\n\nEarly mornings or late evenings are very beautiful. There is ample space for people to sit and enjoy the peaceful and divine surroundings of the temple.",
                    "extracted_snippet": {
                        "original": "Very beautiful Shiv mandir in the middle of hustle bustle of Pune city. The premises is very big, its difficult to imagine there is such big temple in densely packed area of Pune.\n\nThe temple is maintained very well. Premises are very clean and neat. Apart from the main Shiv mandir, there are a number of other small temples of other deities.\n\nEarly mornings or late evenings are very beautiful. There is ample space for people to sit and enjoy the peaceful and divine surroundings of the temple."
                    },
                    "details": {
                        "visited_on": "Weekend",
                        "wait_time": "No wait",
                        "reservation_recommended": "No"
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUM3dm92VWh3RRAB!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgIC7vovUhwE%7CCgwIvcD7tQYQoNSA_wI%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "4 weeks ago",
                    "iso_date": "2024-08-16T05:14:37Z",
                    "iso_date_of_last_edit": "2024-08-16T05:14:37Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipMnJI0x05t3aHA3iD2C6oqGA4Auasmxzy7sY_x-=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOcPyGtsOxB67kSQ-9BLH5DWnjzJ-ulRjUDva9_=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNPj1NgjIXjljNr1CNL-P_YOjGUpPUa515iCctM=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMHWeNLGK6rwxshc54qxlwnQz1kNANL3iXBWCj4=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNrt9zi5Ded2AkDPEbbpQtpJ8Vu50X1P9NF71C5=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipP-Tf_cVvQd9EKNh4oyl8e-RnwmcCtzCvPqdcyU=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChdDSUhNMG9nS0VJQ0FnSUM3dm92VWh3RRAB",
                    "user": {
                        "name": "Bullet Foodie",
                        "link": "https://www.google.com/maps/contrib/115969431229943485706?hl=en-US",
                        "contributor_id": "115969431229943485706",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjVfTXuMqA7OqZt74yJR3wtgbk-6mwCXdt_sTDYwT3bM9zj4xlU=s120-c-rp-mo-ba5-br100",
                        "local_guide": True,
                        "reviews": 108,
                        "photos": 517
                    },
                    "snippet": "Very peaceful and historical temple of Shiva, must visit here it is peshvekalin temple.\n\nYou will get to see the beauty of ancient temple.",
                    "extracted_snippet": {
                        "original": "Very peaceful and historical temple of Shiva, must visit here it is peshvekalin temple.\n\nYou will get to see the beauty of ancient temple."
                    },
                    "details": {
                        "visited_on": "Public holiday",
                        "wait_time": "No wait",
                        "reservation_recommended": "No"
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSURqM2VDaGlRRRAB!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgIDj3eChiQE%7CCgwItsDjsQYQgPLD1AI%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "4 months ago",
                    "iso_date": "2024-05-06T13:47:42Z",
                    "iso_date_of_last_edit": "2024-05-06T13:50:46Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipNqldwrAun8xIS0hIQpElbMgf_hi_10wTbvoE8X=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipN5AtXHNJP7qFkuvEmz_ogNRmf7hekQxBXjlW5B=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOjZgfxt8EKesiy4BWh4yRrO2x26FPEExHAlAhw=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipN6iTC5bxfaTjOQf3uajq6YtQVcUni6LgDSa_lP=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChdDSUhNMG9nS0VJQ0FnSURqM2VDaGlRRRAB",
                    "user": {
                        "name": "Lalit Pandhare",
                        "link": "https://www.google.com/maps/contrib/105582644189368858649?hl=en-US",
                        "contributor_id": "105582644189368858649",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjWDswICs0DYNh9TsLPlwJz_nkKSvToGPvazg_o7mpXu9GSNMp5U=s120-c-rp-mo-ba3-br100",
                        "local_guide": True,
                        "reviews": 62,
                        "photos": 55
                    },
                    "snippet": "A beautiful place to visit in Pune.The deep connection towards God Shiva \ud83d\udc97.The Shri Omkareshwar Temple in Pune is truly a magnificent and spiritually uplifting place. As soon as you step foot inside the temple grounds, you can feel a sense of peace and tranquility wash over you. The architectural beauty of the temple is awe-inspiring, with its intricate carvings and towering spire reaching towards the heavens.",
                    "extracted_snippet": {
                        "original": "A beautiful place to visit in Pune.The deep connection towards God Shiva \ud83d\udc97.The Shri Omkareshwar Temple in Pune is truly a magnificent and spiritually uplifting place. As soon as you step foot inside the temple grounds, you can feel a sense of peace and tranquility wash over you. The architectural beauty of the temple is awe-inspiring, with its intricate carvings and towering spire reaching towards the heavens."
                    },
                    "details": {
                        "visited_on": "Weekend",
                        "wait_time": "No wait",
                        "reservation_recommended": "No"
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUMxNGRlcmtnRRAB!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgIC14derkgE%7CCgwIx67ErAYQ0IrpmgM%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "8 months ago",
                    "iso_date": "2023-12-31T07:24:14Z",
                    "iso_date_of_last_edit": "2023-12-31T07:24:55Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipPXTzwOflZ2FVlRt7VDjfcpY3SEh1zlnD7vYPgi=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipO4bNJ3l1xhfoV6wuIOscr1cwj6cQUDKJDA5pke=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPHwxIid3O_dWMFlYshmC9whGuS8g-aX5QG7Q4L=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMhqPC60svOYC0upho1uCV0J_X8QAUrdfYNn_Ao=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMC-Ch_zBr2yk7Mdnkpe02ohpahYGvkrGeKsDm-=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNqx8z7r41DQm6Smpoj9tfxmP3tjN-jTaYqC4xV=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPx6JFaHVCuT2-Jzd9mdZzZyvdKpmie7OyGs3ne=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPqY-5rOKgVVGPYgdKHgJJNifWmVtvqi0WqYhcp=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOxXxeFOhse2cEZcdMAjfm9X5J-kPj_-xUQGqNV=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNxUe79pBI1RoK1RIzDSvvNAR5FMXEvWbewP6pH=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMfHRalcQkjtJ5Pdhz4ZQH-DCIi7WbBTvM3W7Dg=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMHJ3xCbmWeRqMebrXs0Ya3qVhUBHWTqtLkBfPo=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPZ-O7uPHS7IiHY8FAl8Zsuf2TWpi9MxuO5-a22=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNrL-hbKiqHjDqmgVAr9NltKzT234sjnOZRUf0a=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOUTxg0rOZlYwFA9O6KK83OqlLMz1E6xHqs4H2R=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNqCb1uqpknz1ti0uhNt0f2Fye0YC1PGGuRfCB_=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNP9pM8pssK2B31JKZ5eVtRxHx-iyIivOjb8tFj=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMlGnyjbqkvIiiiSRRw0_wsWyCvhlVbkWiAj12I=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPLj7uVxFUixQ6oeXQYWlMQWZoEbqyp18Vdpuf4=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOjHZ-BQcOsWJpDmNkoN0NRaO5O-7P0bo7OMzrf=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPce5ie6Y-M9oCnMjofPqfQMO7-8VdlgerfjDpE=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNEvptft5ZP3cv1BLtMfgRsIB4MqMypnbCyDe_d=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPzDw4bbYqdLccozt4-xXAIs9gu7TUNVMHPXAYP=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOqUjHkkeMh3lYU5u_3k70mnsI8UJPw3qNpNEgZ=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPSxsXe0Xj51fDP6cegpi9BWqtawjnoOWoOvFCG=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChdDSUhNMG9nS0VJQ0FnSUMxNGRlcmtnRRAB",
                    "user": {
                        "name": "John Paul",
                        "link": "https://www.google.com/maps/contrib/101926218302229462114?hl=en-US",
                        "contributor_id": "101926218302229462114",
                        "thumbnail": "https://lh3.googleusercontent.com/a/ACg8ocJ_FSqU-LBI6Aa2R3R4NiptX2t31js1OmpRIquY4OTnoiIv5Q=s120-c-rp-mo-ba5-br100",
                        "local_guide": True,
                        "reviews": 73,
                        "photos": 495
                    },
                    "snippet": "My View: Trust me..! You will definitely end up having a unique experience when you visit this temple. Best time: Early mornings to get the positive vibes.\n\nI visited this temple on 30th Dec'23 for the first time and the moment I entered it's a different experience altogether. You will definitely be satisfied from a devotional perspective.\n\nAvoid 4 wheelers as there is tight parking, 2 wheelers and autos are best way to get to this place. Around 2 kms you have plenty of food joints and do some nice shopping at reasonable rates.",
                    "extracted_snippet": {
                        "original": "My View: Trust me..! You will definitely end up having a unique experience when you visit this temple. Best time: Early mornings to get the positive vibes.\n\nI visited this temple on 30th Dec'23 for the first time and the moment I entered it's a different experience altogether. You will definitely be satisfied from a devotional perspective.\n\nAvoid 4 wheelers as there is tight parking, 2 wheelers and autos are best way to get to this place. Around 2 kms you have plenty of food joints and do some nice shopping at reasonable rates."
                    },
                    "details": {
                        "visited_on": "Weekend",
                        "wait_time": "No wait",
                        "reservation_recommended": "No"
                    },
                    "likes": 3
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChdDSUhNMG9nS0VJQ0FnSUNqLXFfUTZRRRAB!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgICj-q_Q6QE%7CCgwIyPGPsQYQ0LOiwQE%7C?hl=en-US",
                    "rating": 4.0,
                    "date": "4 months ago",
                    "iso_date": "2024-04-20T17:18:00Z",
                    "iso_date_of_last_edit": "2024-04-20T17:18:00Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipOBTSz6WMQg_XAeuPqO5V187EoW_8CSr40xDMug=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChdDSUhNMG9nS0VJQ0FnSUNqLXFfUTZRRRAB",
                    "user": {
                        "name": "Subodh Lawand",
                        "link": "https://www.google.com/maps/contrib/106121610785035330250?hl=en-US",
                        "contributor_id": "106121610785035330250",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjUmv1AmtDyd6HEA4IH1vUcioHyQjQaFTsK2BI-fspWyXCl5tZQ7=s120-c-rp-mo-ba4-br100",
                        "local_guide": True,
                        "reviews": 42,
                        "photos": 55
                    },
                    "snippet": "The temple is a truly captivating spiritual haven. Its majestic architecture, adorned with intricate carvings and vibrant colors, is a testament to the rich cultural and historical significance it holds. Upon entering, one is enveloped in a profound sense of peace and serenity, making it an ideal place for introspection and spiritual renewal.",
                    "extracted_snippet": {
                        "original": "The temple is a truly captivating spiritual haven. Its majestic architecture, adorned with intricate carvings and vibrant colors, is a testament to the rich cultural and historical significance it holds. Upon entering, one is enveloped in a profound sense of peace and serenity, making it an ideal place for introspection and spiritual renewal."
                    },
                    "likes": 0
                },
                {
                    "link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sChZDSUhNMG9nS0VJQ0FnSUNOdHBMVFlnEAE!2m1!1s0x0:0x90646f988cfb5dd9!3m1!1s2@1:CIHM0ogKEICAgICNtpLTYg%7CCgwI2eyOrQYQgOOG7QE%7C?hl=en-US",
                    "rating": 5.0,
                    "date": "7 months ago",
                    "iso_date": "2024-01-14T10:24:25Z",
                    "iso_date_of_last_edit": "2024-01-14T10:24:25Z",
                    "images": [
                        "https://lh5.googleusercontent.com/p/AF1QipM3ZyfZJw2DAuebAajGWtu6fFg9WycSr1W0iHlq=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipNBg5fMbnGbgiPxo4gMbb_0jr8ozeuESRpkTyZC=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMFgwY9ShrgmNsKs9hDEz7Q1XV1qN8Nt0IbKGQq=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipM6jT36N8IqgrWMvI8n5iwWAzbhQd7MPcvABclI=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipONkw6sl0VkCoeVH9Othybt74v6rnzWiV3HNhj8=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMu8B6atRZofV_nUQR19-PshIkcoBjEphE3geux=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMdVtBgyDToAL6ZOJsfh6k9MBS7tM0K7wfd0nT_=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipOfXWlP-wQXbz7jwUU8rSduvu7WoFdPVD0WdEa9=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipMfdS36aAaroXCOLLY9BsaOLeC4vyW5D3mwEqxu=w150-h150-k-no-p",
                        "https://lh5.googleusercontent.com/p/AF1QipPCWiNMfRl9pZRMX6pR8kn_wOnPmDRwjt2jQ3uo=w150-h150-k-no-p"
                    ],
                    "source": "Google",
                    "review_id": "ChZDSUhNMG9nS0VJQ0FnSUNOdHBMVFlnEAE",
                    "user": {
                        "name": "Rajesh Mali",
                        "link": "https://www.google.com/maps/contrib/101760710822582813748?hl=en-US",
                        "contributor_id": "101760710822582813748",
                        "thumbnail": "https://lh3.googleusercontent.com/a-/ALV-UjVyHyLqTMWhbvk7iYKsZz3waM3XQIx5BiOIDXf1Wp3H9RpamlaS=s120-c-rp-mo-ba4-br100",
                        "local_guide": True,
                        "reviews": 22,
                        "photos": 118
                    },
                    "snippet": "\ud83e\uddd8\ud83c\udffb\ud83e\udd8bI visited the Shree Omkareshwar Hindu Temple, and it was a spiritually enriching experience. The temple's architecture was awe-inspiring, creating a serene atmosphere for worship. The priests were knowledgeable and offered insightful explanations of the rituals. The beautiful chanting and rituals enhanced the sense of tranquility. The temple grounds were well-maintained, and the community was warm and welcoming. Whether you seek spiritual solace or cultural exploration, omkareshwar Temple provides a serene sanctuary for all.\ud83d\udc3f\ufe0f\u2764\ufe0f",
                    "extracted_snippet": {
                        "original": "\ud83e\uddd8\ud83c\udffb\ud83e\udd8bI visited the Shree Omkareshwar Hindu Temple, and it was a spiritually enriching experience. The temple's architecture was awe-inspiring, creating a serene atmosphere for worship. The priests were knowledgeable and offered insightful explanations of the rituals. The beautiful chanting and rituals enhanced the sense of tranquility. The temple grounds were well-maintained, and the community was warm and welcoming. Whether you seek spiritual solace or cultural exploration, omkareshwar Temple provides a serene sanctuary for all.\ud83d\udc3f\ufe0f\u2764\ufe0f"
                    },
                    "details": {
                        "visited_on": "Weekday",
                        "wait_time": "No wait",
                        "reservation_recommended": "No"
                    },
                    "likes": 4
                }
            ],
            "serpapi_pagination": {
                "next": "https://serpapi.com/search.json?engine=google_maps_reviews&hl=en&next_page_token=CAESBkVnSUlDQQ%3D%3D&place_id=ChIJ45xFN3rAwjsR2V37jJhvZJA",
                "next_page_token": "CAESBkVnSUlDQQ=="
            }
        }

        review = []
        if(len(result["reviews"])>10):
            count = 10
        else:
            count = len(result["topics"]
        
        for i in range(0,count):
            review.append(result["reviews"][i]['extracted_snippet']['original'])
        reviews.append(review)

        topic = []
        for i in range(0,len(result["topics"])):
            topic.append(result["topics"][i]['keyword'])
        topics.append(topic)


    data = {
        'place_id': place_id,
        'reviews': reviews,
        'topics': topics
    }

    df = pd.DataFrame(data)
        
    # saving the dataframe
    df.to_csv(f'meta_csv/review_data_{con.search}.csv')
    print(f"{con.search}_extracted successfully")
