select user_id,email
from Users
where email like '%@%.com' and email not like '%.%@%.com'