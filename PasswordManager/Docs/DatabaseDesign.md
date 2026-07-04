ID, Service, Username and Password 

ID: The unique row number to identify.
Service: the app or website the password corresponds
Username and Password

Primary Key -> ID
Why ? Because there can be same username, and ID is unique

EG: 
ID  Serive   Username   Password
1   GOOGLE   user111    2322 
2   Facebook user111    swne

Username is same, but ID can distinguish them

ID: Integer Unique Autoincrement
Service, Username and Password: TEXT, max limit 1,000,000,000 bytes, very flexible but we could have also choose VARCHAR(50) but VARCHAR(50) is NOT enforced in SQLite so TEXT was a wise option with constrains and I can try something new too 

Constrains: Username !> 20, Service !> 20, Password !> 20



