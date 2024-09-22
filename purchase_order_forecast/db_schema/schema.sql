create table purchaseorder (
    cost_center varchar(2),
    risk varchar,
    risk_category varchar,
    po_num varchar(10),
    po_owner varchar,
    vendor_num varchar(4),
    po_amount_usd integer,
    forecast_amount_usd integer,
    invoice_to_date_usd integer
);

insert into purchaseorder (  cost_center, 
            risk, 
            risk_category, 
            po_num, 
            po_owner, 
            vendor_num, 
            po_amount_usd,
            forecast_amount_usd,
            invoice_to_date_usd
)
values ('c6', 'risk', 'in-sufficient funds', 1000055555, 'Stanley','S456', 10000000,20000000, 9999999),
        ('c6', 'safe', 'normal', 1000055558, 'Stanley','X456', 10000000,10000000, 99999),
        ('c6', 'risk', 'in-sufficient funds', 1000055559, 'JPMC','J456', 50000000,60000000, 30000000),
        ('c6', 'safe', 'normal', 1000055560, 'JPMC','J456', 30000000,20000000, 10000000);

select
    *,
    (po_amount_usd-forecast_amount_usd) as accrual
from
    purchaseorder;

