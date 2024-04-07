Diskovery Webstore Documentation –

Sales Analysis Integration


# Contents

[1 - The Concept](#_toc151231282)

[2 - The Structure](#_toc151231283)

[3 - The Database](#_toc151231284)

[3.1 - The Collections](#_toc151231285)

[3.2 - The Documents Structure](#_toc151231286)

[3.3 The Indexes](#_toc151231287)

[4 - The Server](#_toc151231288)

[5 - The Lambda Function](#_toc151231289)

[6 - The Buckets](#_toc151231290)

[7 - The analysis](#_toc151231291)

[8 - The Notification System](#_toc151231292)

[9 - The CI (Continues Integration)](#_toc151231293)





## <a name="_toc151231282"></a>1 - The Concept
“Diskovery” (pun intended) is an ecommerce store that sells storage disks as a mediator. All its sales and traffic are through the internet, and it does not have a physical store.

It’s a classic start-up business with a relatively low starting capital. To analyze the development of the business, the CEO decides to implement a cloud hosted integration along with a versatile database, as the low budget closes the door for the physical data center option.

When it comes to cloud solutions, there are a lot of players in the field, with many strengths and weaknesses for each one, but for this project for unimportant convenient reasons the exchangeable route of AWS has been chosen.

## <a name="_2_-_the"></a><a name="_toc151231283"></a>2 - The Structure
The following diagram aims to contextualize the whole integration for each application involved in this project.

The main applications used are some basic and intermediate AWS services along with a MongoDB database.

The main component is the EC2 instance, which triggers periodically two scripts for the whole project to come to life.

![image](https://github.com/AlexandrosPal/DiskoverStoreProject/assets/103060739/59d8f924-38c7-4f83-83b0-6bc493687136)

The life cycle of the application compiles around these scripts. The first one aims to populate the database with data regarding the sales and the restocks from the suppliers, while the second one is to retrieve all the data from the database, analyze it, upload a report to a bucket and send a notification regarding the process.

## <a name="_toc151231284"></a>3 - The Database
For this project, either a relation or a non-relational database would work fine with not big differences. “Diskovery” though is a start-up business which is going to be constantly evolving and changing, so the more versatile solution is going with a document-based database, like MongoDB.

### <a name="_toc151231285"></a>3.1 - The Collections
The database is split into 3 collections: **products** (basic product Information), **prod\_details** (more details about the products) and **sales**.

The distinction between the “products” and the “prod\_details” is to optimize the RAM and the read speed when querying the “products” collection to produce the reports. The “details” collection does not have an immediate use for this specific application for the time being, but it is something that can prove useful is the future.

This distinction is of course using the “Subset” database design pattern, as  per MongoDB (<https://www.mongodb.com/blog/post/building-with-patterns-the-subset-pattern>).

The sales collection is a capped type with a max of 350 documents and size of 20000 bytes. Everyday 20-50 sales documents will be inserted into the database, thus 50 \* 7 = 350 documents max, with each one having fixed [fields](#document_structure), thus the 20000 size in bytes.

### <a name="_toc151231286"></a>3.2 - The Documents Structure
The documents for the sales collection have a fixed structure at the time of first building the database:

|**KEY**|**REQUIRED**|**TYPE**|**EXAMPLE**|
| :- | :- | :- | :- |
|order\_id|true|string|“O001”|
|product\_id|true|string|“D001”|
|quantity|true|number|5|
|price|true|number|35|
|revenue|true|number|175|
|date|true|date|“2023-10-29T18:00:00”|



Below is the table for the “products” collection:

|**KEY**|**REQUIRED**|**TYPE**|**EXAMPLE**|
| :- | :- | :- | :- |
|\_id|true|string|“O001”|
|name|true|string|“D001”|
|price|true|number|35|
|instock|true|number|63|

And for the “product\_details”:

|**KEY**|**REQUIRED**|**TYPE**|**EXAMPLE**|
| :- | :- | :- | :- |
|product\_id|true|string|“D001”|
|price\_unit|true|string|“dollars”|
|type|true|string|“SSD”|
|storage|true|number|512|
|storage\_unit|true|string|“GB”|
|manufacturer|true|string|“Samsung”|
|read\_speed|true|number|560|
|read\_speed\_unit|true|string|“MB/sec”|
|write\_speed|true|number|530|
|write\_speed\_unit|true|string|“MB/sec”|
|size|true|number|2\.5|
|size\_unit|true|string|“inches”|

### <a name="_toc151231287"></a>3.3 The Indexes
In the analysis part, where the second EC2 script will run and query the MongoDB database to generate the plots, certain commands will be used to get the necessary data. In order to make them more efficient in terms of read speed, MongoDB supports the use of indexes. 

As mentioned in chapter <a name="document_structure"></a>[7 - The analysis](#_7_-_the), the 4 diagrams will be regarding the most sold products, the most popular products, the product that generated the most revenue and the most profitable dates. Thus, the indexes needed will be:

- product\_id + quantity
- product\_id + orders
- product\_id + revenue
- date + revenue


## <a name="_toc151231288"></a>4 - The Server
### 4\.1 The Overview
The main server is hosted on an AWS EC2 virtual machine of t2.micro type and an Amazon Linux operating system. It also has 1 vCPU, 0.5GB of memory and 8GB of EBS storage attached. 

In terms of networking, it is enclosed in a private subnet with a Security Group blocking all public access accept a specific IP address allowing SSH connections. Furthermore, for the identification of the SSH connection a .pem file is required as a keypair.

### 4\.2 The Scripts
The Instance is responsible for periodically triggering 2 scripts, each one responsible for a separate part of the flow. As shown in the [diagram](#_2_-_the), the first script will run everyday and it will upload a json file in an S3 Bucket, which represents the sales made that day. For reference, there is an example inside the “data” folder of the [project’s GitHub repository](https://github.com/AlexandrosPal/DiskoverProject), as the value of the “sales”.

The second script is triggered once a week on Sunday and it corresponds to the analysis part of the flow. It gathers data from the MongoDB database with certain commands and it builds 4 main plots and diagrams. These plots are exported in a single PDF file, which is put in a 2 S3 Buckets: the “diskover-archive” bucket (for all of the past groups of plots, including the current one), and the “diskoveranalytics.live” (only for the current group of plots).

## <a name="_toc151231289"></a>5 - The Lambda Function
The Lambda function is used as a mediator between the server and the database. It receives the json file from the input S3 bucket and performs 3 actions:

1. Inserts the objects inside the json file inside the sales collection of the database,
1. Transfers the json file from the input bucket to the output bucket,
1. Sends an email notification to a SNS Topic regarding the outcome of the process, either success or fail)

## <a name="_toc151231290"></a>6 - The Buckets
The application uses in total 4 buckets, two for each script. 

The “input” bucket is used as a manual way to decouple the server and the lambda function.

The “output” bucket is used for viewing the “sales.json” file after each trigger of the first script.

The “archive” bucket is used for storing all the old reports generated by the second script.

Finally, the “diskoveranalytics.live” bucket is to view the latest report generated. This report is public for everyone to watch and can be found on the s3 default object link: https://s3.eu-central-1.amazonaws.com/diskoveranalytics.live/Sales_Report.pdf

## <a name="_7_-_the"></a><a name="_toc151231291"></a>7 - The analysis
The second script is responsible for fetching data from the MongoDB database and process them to generate the plots of the reports. The analysis per se is simple and nothing complicated. It consists of some basic KPI: 

- Most sold items
- Most popular items
- Most profitable items
- Most profitable dates

As the business grows and the demands for growth grow too, more analysis will be needed.


## <a name="_toc151231292"></a>8 - The Notification System
As part of the first script, there is a notification system that sends the status of the script regarding the outcome. If it is a successful the email will notify with “Lambda ran successfully”, but if something went wrong at either end, EC2 server, Lambda script, MongoDB collection, the notification will read “Lambda function failed due to …” plus the reason of the failure.


## <a name="_toc151231293"></a>9 - The CI (Continues Integration)
The implementation of features, changes, bugfixes etc. consists of performing the tasks outside the server instance. As security best practice the server should be accessed for everyday tasks.

Thus, when merging changes towards the main branch, a GitHub Action has been setup in the “.github“ folder, where in case of a push in the main branch, an agent logs in to the server using ssh, navigates to the right folder and pulls the changes in order for them to take effect. The information about the ssh key, the host and the port are located inside GitHub Secrets for actions.
