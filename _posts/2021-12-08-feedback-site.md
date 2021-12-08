---
date: 2021-11-28 20:12:00
layout: post
title: Basic implementation of the feedback system
description: Sending and viewing feedbacks
image: FYP-blog/assets/img/uploads/feedback_site.png
category: blog
author: Joe Siu
paginate: true
---
When in game, press F8 will opens up the feedback form, where players can type the comment and select the type and rating. Upon pressing the submit button, the feedback will then be send to the Firebase server. A green notification will also shows up to tell player the feedback had been sent.

![](FYP-blog/assets/img/uploads/feedback_success.png)



However, if the feedback failed to send to the server (e.g. no internet), a red notification banner will show instead, telling players the error.

![](FYP-blog/assets/img/uploads/feedback_fail.png)



All submitted feedbacks can then be viewed at <https://joesiu.github.io/FYP-feedback-site/>.

![](FYP-blog/assets/img/uploads/feedback_site.png)