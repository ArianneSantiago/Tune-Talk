# Tune Talk
![]()
**is an Album Review Website that allows user to share their insights and opinions on various albums. Users can create accounts, write detailed reviews for album, and provide individual ratings. The average rating for each album is dynamically calculated based on the collective reviews, providing users with an overall perspective. Dive into the world of music exploration and join the community discussion on Tune Talk!**

![alt text]()

Deployed version can be viewed [here][1].
[1]: https://tune-talk-app-02b083d29396.herokuapp.com/
---
# UX Design
---
### Overview

## Design

# User Stories



# Wireframe
---
![alt text]()

*Mobile wireframe*
![alt text](https://github.com/ArianneSantiago/Tune-Talk/blob/main/Mobile%20Wireframe.png)

*Logged in Browse Albums*
![alt text](https://github.com/ArianneSantiago/Tune-Talk/blob/main/List%20of%20Album.png)
---

# Database Entity Relationship Diagram

![alt text](https://github.com/ArianneSantiago/Tune-Talk/blob/main/Database%20ER%20Diagram%20.png)

- After deciding on what kind of project and features I wanted to implement I used a lucidchart to plan the database structure.
- The above diagram is serving as an initial guide to indicate the types and relationships between data stored

#### Data Models

>  User Model from Django
| Key | Name | Field |
| -- | -- | -- |
| PK | user_id | |
| x | FirstName | |
| x | FirstName | |
| x | FirstName | |


> Album Model
| Key | Name | Field |
| -- | -- | -- |
| x | title | CharField |
| x | artist | CharField |
| x | release_year | IntegerField |
| x | genre | CharField |
| x | featured_image | CloudinaryField |
| x | status | IntegerField |
| x | created_on | DateTimeField |
| x | updated_on | DateTimeField |

> Review Model
| Key | Name | Field |
| -- | -- | -- |
| FK | album | ForeignKey |
| FK | user | ForeignKey |
| x | content | TextField |
| x | created_on | DateTimeField |


> Rating Model
| Key | Name | Field |
| -- | -- | -- |
| FK | user | ForeignKey |
| FK | album | oreignKey |
|  | rating | IntegerField |

---
# Flow Chart
![Flow Chart](media/TuneTalk%20Flow%20Chart%20(1).png)

During the process of creating the app, I found the flow chart to be an efficient way to make important decisions. It helped me narrow down which decisions were important for both the users and the admin, and it also helped me establish the appropriate authentication. Additionally, the flow chart allowed me to determine which features were the most essential for the app to function properly.
---
# Validation

# HTML
---
| Page | W3C URL | Screenshot | Notes |
| -- | -- | -- | -- |
| Home | W3C |  | Pass: No Errors |
| Album List | W3C |  | Pass: No Errors |
| Add Album | W3C |  | Pass: No Errors |
| Album Detail | W3C |  | Pass: No Errors |
| Edit Review | W3C |  | Pass: No Errors |
| Sign In | W3C |  | Pass: No Errors |
| Register | W3C |  | Pass: No Errors |

# CSS
---
I have used the recommended CSS Jigsaw Validator to validate my CSS file.
| Page | W3C URL | Screenshot | Notes |
| -- | -- | -- | -- |
| style.css | W3C |  | Pass: No Errors |
---
Python
---
I have used the recommended PEP8 CI Python Linter to validate all of my Python files.
| Page | W3C URL | Screenshot | Notes |
| -- | -- | -- | -- |
| Home | W3C |  | Pass: No Errors |
|  | W3C |  | Pass: No Errors |
|  | W3C |  | Pass: No Errors |
|  | W3C |  | Pass: No Errors |
|  | W3C |  | Pass: No Errors |
---
# Responsiveness
---
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptop:
⋅⋅* Lenovo ideapad 14" screen

Mobile Device:
⋅⋅* Android Device Oneplus

Browser Compatibility:
>  I have tested the site using the following browsers:

⋅⋅* Google Chrome
![google chrome]()

⋅⋅* Microsoft Edge
![microsoft edge]()

Mobile Device:
![]()
---
# Testing
---
# 





