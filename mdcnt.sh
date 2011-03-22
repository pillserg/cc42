#!/bin/bash
python manage.py modelscount > grep error: *  > $(date +%Y-%m-%d.dat)




