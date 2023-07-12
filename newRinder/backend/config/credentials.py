from flask import Flask
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "Ad7IB5jSXxN87nNaM974VIyiwEHLF0E23b-LRb2dhXtMtvvg3E3CdX6uSvy-Wxa8wFEwl2B5k9P946_Q",
    "client_secret": "EHAsV0IHZfNcT46_sxAB77uGmB_Wnc9Rkj8jkGjHJMwTcVCJ_WlS84E0DzocVdhbm0_CncPsljo_24W-"
})
