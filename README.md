# TEST TASK TREE-MENU
________
Simple and understandable. You add new menus and items in Django admin and they appear on the main page automatically, you just choose what menu to go and then you are being redirected to the required URL.
____
To not waste your time I have turned around my app with docker&docker-compose with YOUR PREFERABLE DB(POSTGRESQL). So there are some steps to have this project on your local machine:

```
git clone https://github.com/Povladislav/Tree.git
```
```
sudo docker-compose build
```
```
sudo docker-compose up
```

# P.S as I did not share my .env file to you and to ensure,that your database will work, unfortunately, you need to create your own, or just pass "raw" data to settings of your DB(treemenu->settings.py)
