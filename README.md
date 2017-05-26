## Student Technology Hour Manager

If you're new to django, please check out [this link](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django), as you'll learn everything you need to know there.

### Info:

* Dispatching should be done per app. IE hour manager's static files and urls.py are seperate from other apps. There *should not* be a general static folder unless it is used for request "/"

* This uses military time, as that is the easiest way for the database models to *handle* the time. This should not be changed, or attempted to be changed. 

