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





select current_region();


Every Snowflake account has THE SNOWFLAKE database included in the account
It is good to be aware that another name for "THE SNOWFLAKE database" is "the Account Usage Share." 



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




Other courses and information sources are available and may be a better fit for your needs and preferences. 

For non-hands on courses and certification preparation guides, see other courses on this site. 
For advanced tutorials, go to quickstarts.snowflake.com 
For instructor-led training go to training.snowflake.com
For documentation go to docs.snowflake.com
For forum discussions and technical support go to community.snowflake.com 
