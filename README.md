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


Other courses and information sources are available and may be a better fit for your needs and preferences. 

For non-hands on courses and certification preparation guides, see other courses on this site. 
For advanced tutorials, go to quickstarts.snowflake.com 
For instructor-led training go to training.snowflake.com
For documentation go to docs.snowflake.com
For forum discussions and technical support go to community.snowflake.com 
