#!/usr/bin/env bash
mkdir -p ./keys
read -p "Press [Enter] to create instance"
ansible-playbook -i inventory create_instance.yml -v
inventory/ec2.py --refresh-cache

read -p "Press [Enter] to prepare environment"
ansible-playbook -i inventory prepare_env.yml -v

read -p "Press [Enter] install monitoring service"
ansible-playbook -i inventory create_monitoring.yml -v
monitor_ip=$(inventory/ec2.py  --list|grep -A1 tag_Name_Proxy|grep "[0-9]\+")
echo "Вы можете вписать в файл /etc/hosts"
echo "${monitor_ip} monitor.myserver.org"
echo "И открыть панель мониторинга для просмотра состояния виртуальных машин"
