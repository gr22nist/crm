-- .mode csv
-- .headers ON

-- .import user.csv users
-- .import order.csv orders
-- .import orderitem.csv orderitems
-- .import item.csv items
-- .import store.csv stores

-- CREATE TABLE IF NOT EXISTS "users"(
--     "Id" TEXT PRIMARY KEY,
--     "Name" TEXT NOT NULL,
--     "Gender" TEXT NOT NULL,
--     "Age" INTEGER,
--     "Birthdate" DATE,
--     "Address" TEXT,
--     UNIQUE("Name", "Address")
-- );

-- CONTRAINT 를 설정하는 과정...

-- CREATE TABLE IF NOT EXISTS "stores"(
--     "Id" TEXT PRIMARY KEY,
--     "Name" TEXT NOT NULL,
--     "Type" TEXT,
--     "Address" TEXT
-- );

-- CREATE TABLE orders (
--     "Id" TEXT PRIMARY KEY,
--     "OrderAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     "StoreId" TEXT NOT NULL,
--     "UserId" TEXT NOT NULL,
--     FOREIGN KEY (StoreId) REFERENCES stores(Id),
--     FOREIGN KEY (UserId) REFERENCES users(Id),
--     CHECK (OrderAt <= CURRENT_TIMESTAMP)
-- );

-- CREATE TABLE IF NOT EXISTS "items"(
--     "Id" TEXT PRIMARY KEY,
--     "Name" TEXT NOT NULL,
--     "Type" TEXT,
--     "UnitPrice" INTEGER CHECK (UnitPrice >= 0)
-- );  

-- CREATE TABLE IF NOT EXISTS "orderitems"(
--     "Id" TEXT PRIMARY KEY,
--     "OrderId" TEXT NOT NULL,
--     "ItemId" TEXT,
--     FOREIGN KEY ("OrderId") REFERENCES "orders"("Id") ON DELETE CASCADE,
--     FOREIGN KEY ("ItemId") REFERENCES "items"("Id")
-- );

-- UPDATE users
-- SET gender = '여성'
-- WHERE gender = 'Female';

-- UPDATE users
-- SET gender = '남성'
-- WHERE gender = 'Male';

-- UPDATE items
-- SET name = '아메리카노'
-- WHERE type = 'Americano Coffee';

-- UPDATE items
-- SET name = '에스프레소'
-- WHERE type = 'Espresso Coffee';

-- UPDATE items
-- SET name = '카페모카'
-- WHERE type = 'Mocha Coffee';

-- UPDATE items
-- SET name = '카푸치노'
-- WHERE type = 'Cappuccino Coffee';
