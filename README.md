# first_streamlit_app
Streamlit App Developed in Snowflake Badge 2 (Data Applications)

API INTEGRATION
Run this code once per Snowflake Trial Account.

use role accountadmin;
create or replace api integration dora_api_integration
api_provider = aws_api_gateway
api_aws_role_arn = 'arn:aws:iam::321463406630:role/snowflakeLearnerAssumedRole'
enabled = true
api_allowed_prefixes = ('https://awy6hshxy4.execute-api.us-west-2.amazonaws.com/dev/edu_dora');


GRADER FUNCTION

use role accountadmin;  
create or replace external function demo_db.public.grader(
      step varchar
    , passed boolean
    , actual integer
    , expected integer
    , description varchar)
returns variant
api_integration = dora_api_integration 
context_headers = (current_timestamp,current_account, current_statement) 
as 'https://awy6hshxy4.execute-api.us-west-2.amazonaws.com/dev/edu_dora/grader'
; 


-- set your worksheet drop lists to the location of your GRADER function
--DO NOT EDIT BELOW THIS LINE - Don't add or take away spaces, do change 'from' to 'FROM' - NO EDITS AT ALL
select GRADER(step,(actual = expected), actual, expected, description) as graded_results from (
SELECT 'DORA_IS_WORKING' as step
 ,(select 223 ) as actual
 ,223 as expected
 ,'Dora is working!' as description
); 



select current_region();

--IT36598
SELECT CURRENT_ACCOUNT();

--Here's code to recreate the "Like a Window" Stage in the DEMO_DB. You can just use the stage from GARDEN_PLANTS if you are using the same Trial account from an earlier workout. 
create stage demo_db.public.like_a_window_into_an_s3_bucket
url = 's3://uni-lab-files';

--And here's a reminder of the syntax for COPY INTO:
copy into my_table_name
from @demo_db.public.like_a_window_into_an_s3_bucket
files = ( 'IF_I_HAD_A_FILE_LIKE_THIS.txt')
file_format = ( format_name='EXAMPLE_FILEFORMAT' );


Every Snowflake account has THE SNOWFLAKE database included in the account
It is good to be aware that another name for "THE SNOWFLAKE database" is "the Account Usage Share." 

no ddl statements on inbound shares
inbound shares import permissions and revoke
inbound shares no updates inserts or deletes

The Account Usage Share is weird because you can't drop or rename it like other inbound shares.

What changes appear on the Shared Data screen because we have dropped the SNOWFLAKE_SAMPLE_DATA database?
Select 2.
Two tiles still appear, but one has a download button.
The database name that appeared on SFC_SAMPLES tile is no longer there.

Which of the following were you able to carry out on the SNOWFLAKE database (The Account Usage Share)?
Unable to rename or drop acct usage share. error - insufficient privs


The real value of consuming shared data is:
Someone else will maintain it over time and keep it fresh
Someone else will pay to store it
You will only pay to query it

What are the names of the 3 Snowflake Sharing Technologies?
Direct Sharing
Snowflake Data Marketplace
Private Exchanges

Why do you think the SNOWFLAKE and SNOWFLAKE_SAMPLE_DATA databases did not show up on the list during your share creation process?
Select 2.

Because I don't have the rights to share the data.
Because you can't share a share


Why do you think the interface does not show the views you created?
Because we created "regular" views instead of "secure" views.


Who could you share your new Outbound Share with?
a) I could share it with Martín Rojas at World Data Emporium (SE59172).
b) I could share it with any account on Azure Canada Central (Toronto) -- if they told me their Account Locator.
c) I could share it with other people taking this course - if they told me their Account Locator.
d) I could share it with anyone, even people with no Snowflake Account -- if I set them up with something called a "Reader Account"


Why couldn't the view that includes the NATIONS table be added to the share?
Because the NATIONS table comes from an Inbound Share (SNOWFLAKE_SAMPLE_DATA)
Because you can't share a share.


If thousands of learners who go through this workshop, and all of them share their Outbound Shares with Martín, will Martín's Database list be impossible to navigate?
No, because Inbound shares (for Martín they are inbound) only show on the list of databases if Martín decides to "get" them.


We often use the words ACCOUNT and USER as if they are interchangeable words. In Snowflake, it is important to keep them separate. Look at the statements below and select the ones that are TRUE.
Select 4.
A Snowflake Trial Account is an ACCOUNT, not a USER.
The name and password entered during the login process is a USER, not an ACCOUNT.
When a USER is created, it provides access to a single ACCOUNT, but an ACCOUNT can have many USERS.
Each learner in this Workshop should have a USER they use to log in to a Snowflake Trial ACCOUNT.


Which of the following are true about sub-accounts (also called Managed Accounts or Reader Accounts)?
Select 4.
I can create a "sub-account" to my Snowflake Trial Account. This is different than just creating a Login/User for my Trial Snowflake Account.
When I create the sub-account it gets its own Account Locator and URL.
I should note both of my account URLs so I can recall which is my trial account and which is the sub-account I manage.
I can create logins or USERS for the sub-account. If I don't write down the User and Password I create for my sub-account login, I don't have any way to retrieve it.







Other courses and information sources are available and may be a better fit for your needs and preferences. 

For non-hands on courses and certification preparation guides, see other courses on this site. 
For advanced tutorials, go to quickstarts.snowflake.com 
For instructor-led training go to training.snowflake.com
For documentation go to docs.snowflake.com
For forum discussions and technical support go to community.snowflake.com 
