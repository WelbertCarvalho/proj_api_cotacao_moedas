insert into datalake.cotacao_btc_brl (
    code, 
    codein, 
    name, 
    high, 
    low, 
    varBid, 
    pctChange, 
    bid, 
    ask, 
    create_date, 
    created_at)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, CURRENT_TIMESTAMP());
