## 使用工具
开源链接测试工具broken-link-checker
https://github.com/stevenvachon/broken-link-checker

## 链接测试过程
```shell
$ blc http://localhost:8000/booksystem/user_info/ -ro
Getting links from: http://localhost:8000/booksystem/user_info/
├───OK─── http://localhost:8000/booksystem/
├───OK─── http://localhost:8000/booksystem/result/
├───OK─── http://localhost:8000/booksystem/login_user/
├───OK─── http://localhost:8000/booksystem/logout_user/
└───OK─── http://localhost:8000/booksystem/register/
Finished! 10 links found. 5 excluded. 0 broken.

Getting links from: http://localhost:8000/booksystem/
Finished! 4 links found. 4 excluded. 0 broken.

Getting links from: http://localhost:8000/booksystem/result/
Finished! 9 links found. 9 excluded. 0 broken.

Getting links from: http://localhost:8000/booksystem/login_user/
Finished! 10 links found. 10 excluded. 0 broken.

Getting links from: http://localhost:8000/booksystem/logout_user/
Finished! 10 links found. 10 excluded. 0 broken.

Getting links from: http://localhost:8000/booksystem/register/
Finished! 10 links found. 10 excluded. 0 broken.

Finished! 53 links found. 48 excluded. 0 broken.
Elapsed time: 0 seconds
```

## 链接测试结果分析
|URL|links|excluded|broken|result|
|---|-----|--------|------|------|
|http://localhost:8000/booksystem/|4|4|0|OK|
|http://localhost:8000/booksystem/result/|9|9|0|OK|
|http://localhost:8000/booksystem/login_user/|10|10|0|OK|
|http://localhost:8000/booksystem/logout_user/|10|10|0|OK|
|http://localhost:8000/booksystem/register/|10|10|0|OK|
