import sys
import os
import requests


def main():
    api = 'https://user-1663601139210:ca7a38b5ab9f21f0593dc4ef5e0fce3dede4d955@glia-computing.api.abeja.io/deployments/1667339232000/services/ser-4a8657920b9e4e9c'
    data = open('IMG_3628.JPG', 'rb').read()
    res = requests.post(url=api,
                        data=data,
                        headers={'Content-Type': 'image/jpeg'})
    print(res.headers)
    print(res.text)


if __name__ == '__main__':
    main()
