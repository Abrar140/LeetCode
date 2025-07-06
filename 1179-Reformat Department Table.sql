# Write your MySQL query statement below

Select id , 
SUM(Case when month = 'Jan' then revenue else null  END ) as Jan_Revenue,
SUM(Case when month =  'Feb' then revenue else null  END ) as Feb_Revenue,
SUM(Case when month =  'Mar' then revenue else null  END ) as Mar_Revenue,
SUM(Case when month =  'Apr' then revenue else null  END ) as Apr_Revenue,
SUM(Case when month =  'May' then revenue else null  END ) as May_Revenue,
SUM(Case when month =  'Jun' then revenue else null  END ) as Jun_Revenue,
SUM(Case when month =  'Jul' then revenue else null  END ) as  Jul_Revenue,
SUM(Case when month =  'Aug' then revenue else null   END ) as Aug_Revenue,
SUM(Case when month =  'Sep' then revenue else null  END ) as  Sep_Revenue,
SUM(Case when month =  'Oct' then revenue else null  END ) as Oct_Revenue,
SUM(Case when month =  'Nov' then revenue else null  END )  as Nov_Revenue,
SUM(Case when month =  'Dec' then revenue else null  END ) as Dec_Revenue

from Department

group by id

