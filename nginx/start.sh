#!/bin/bash
envsubst '$DJANGO_SERVER_ADDR $ALB_URL' < /tmp/default.conf > /etc/nginx/conf.d/default.conf && nginx