ó
DT\c           @   sE  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e j d  e j	   Z
 e
 j e  e
 j e  e
 j e  e
 j e  e
 j e j    e
 j e j j   d d d Z d   Z d   Z d   Z e d	 k rAe d
  Z e d k s-e d k r7e   qAe   n  d S(   iÿÿÿÿNt   cleart   max_timei   s³  
    ââââ    ââââââ  âââââââââ âââ     âââ ââ âââââââââ 
   âââââââ ââââ  ââââ  âââ ââââââ    ââââ âââââ ââ   â 
   ââââ âââââââ  ââââ ââââ ââââââ    ââââââââââ ââââ   
   ââââââ  âââ   ââââ ââââ â ââââ    âââââââ ââ âââ  â 
   âââ  ââââ âââââââ  ââââ â ââââââââââââââââ âââââââââ
   âââââââââ ââââââ   â ââ   â âââ  âââ  â ââ ââââ ââ â
   âââ   â   â â ââ     â    â â â  â â ââ ââ ââ â â  â
    â    â â â â â    â        â â    â ââ ââ â    â   
    â          â â               â  â â  â  â      â  â
         â                                             

Author : Mr.K3R3H
Facebook : Kereh Ronaldo
Github : https://github.com/kereh
Version : 1.0
c         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
g¹?(   t   syst   stdoutt   writet   flusht   timet   sleept   random(   t   textt   puts(    (    s   autolike.pyt   run!   s    c          C   s   t  j d  GHHt d  t d  }  t d  } t j d |  d | d  } t d d	  } | j | j    | j   d
 GHHd  S(   Ni<   s   [*] Kereh Bot Likes   [+] enter your username : s   [+] enter your password : s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6s	   token.logt   ws-   [*] File Saved With Name [1;32mtoken.log[0m(	   t   bannert   centerR   t	   raw_inputt   brt   openR   t   readt   close(   t   usernamet   passwordt   rt   file(    (    s   autolike.pyt   generate'   s    

c          C   s¤  t  j d  GHHt j d  }  t d  } t | d  j   } t j d d  | t j d <t j   } | j   } t	 j
 d  } yÍ Hd	 G| j |  d Gd
 GHHd } d } d } d }	 t j d  }
 |
 rJt d  } t j d d  d | g t j d <t j   } | j   } | GHt j d  | GH|	 GHd GHd GHt j   n d GHWnM t k
 rhd GHn8 t k
 rd GHt j d  n t k
 rd GHn Xd  S(   Ni<   s   https://yolikers.com/s4   [+] input your token file name ( ex : token.log ) : R   t   nri    t   access_tokens   Login Successfuls   [+] Status :[1;32ms   [0ms   [*] Kereh Bot Running...s   [*] We Sending Your Many Likess&   [*] Subscribe My Channel Kereh Channels   [*] Please Wait...s)   https://yolikers.com/like.php?type=statussB   [+] type react [ ex : 'LIKE','LOVE','HAHA','WOW','SAD','ANGRY'] : t    t   typei   s    [+] Response :[1;32mSuccess[0ms%   [+] Sleep For 15 Minute or 900 seconds   [+] Response :[1;31mFailed[0ms   [+] CEK INTERNET CONNECTIONs   [+] Exit...i   s   [+] Failed...(   R   R   R   R   R   R   t   select_formt   formt   submitt   ret   compilet   findallR   R   R   t   exitt   IOErrort   KeyboardInterruptt
   IndexError(   t   at   tokent   tokenst   bt   ct   dt   kontol_messaget   kontol_message1t   kontol_message2t   kontol_message3R   t   reactt   xt   z(    (    s   autolike.pyt   autolike4   sP    	t   __main__s/   [+] DO YOU HAVE ACCESS TOKEN FILE??? [ Y/N ] : t   yt   Y(   R    t	   mechanizet   bs4t   osR   R   R   t	   cookielibt   systemt   BrowserR   t   set_handle_robotst   Falset   set_handle_referert   Truet   set_handle_redirectt   set_handle_equivt   set_cookiejart   LWPCookieJart   set_handle_refresht   _httpt   HTTPRefreshProcessorR   R   R   R4   t   __name__R   t   tanya(    (    (    s   autolike.pyt   <module>   s"   `			-
