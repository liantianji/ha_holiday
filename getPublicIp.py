import sys
import os, requests, json, logging, logging.handlers

def getNewPublicIp():
        _publicIp=''
        url = "http://httpbin.org/ip"
        try:
                response = requests.request("GET", url, timeout=5)
        except Exception as err:
                #self.logger.error('Error - http request error of getLocalPublicIp - {}'.format(err))
                raise RuntimeError(err)
                # return ''

        if response.status_code != 200:
                #self.logger.error('Error - http request error of getLocalPublicIp not 200')
                raise RuntimeError('Error - http request error of getLocalPublicIp not 200')
        # publicIp = response.json().get('ip_addr', '')
        publicIp = response.json().get('origin', '')
        publicIp = publicIp.split(',')
        if not publicIp:
                #self.logger.error('Error - new public ip acquiring failed')
                raise RuntimeError('Error - new public ip acquiring failed')
                publicIp = publicIp[0]
                #self.logger.info('My public ip acquired - {}'.format(publicIp))
                #self.wanip=publicIp[0]

        return publicIp[0]	
