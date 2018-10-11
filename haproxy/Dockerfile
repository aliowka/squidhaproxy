FROM haproxy:1.8
RUN apt-get update && apt-get install --no-install-recommends -y rsyslog ca-certificates
ADD haproxy.cfg /etc/haproxy/haproxy.cfg
EXPOSE 9000 8013 8014 8043
CMD update-ca-certificates && /etc/init.d/rsyslog start && haproxy -f /etc/haproxy/haproxy.cfg && tail -F /var/log/haproxy.log
