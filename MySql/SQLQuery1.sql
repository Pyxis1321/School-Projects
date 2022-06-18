--CREATE TABLE Category
--(
--  CategoryID INT NOT NULL,
--  Category VARCHAR(100) NOT NULL,
--  PRIMARY KEY (CategoryID)
--);

--CREATE TABLE Allergens
--(
--  AllergenID INT NOT NULL,
--  Name VARCHAR(100) NOT NULL,
--  PRIMARY KEY (AllergenID)
--);

--CREATE TABLE Sizes
--(
--  SizeID INT NOT NULL,
--  Size VARCHAR(15) NOT NULL,
--  PRIMARY KEY (SizeID)
--);

--CREATE TABLE Menu
--(
--  Name VARCHAR(50) NOT NULL,
--  FoodID INT NOT NULL,
--  CategoryID INT NOT NULL,
--  PRIMARY KEY (FoodID),
--  FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
--  on delete cascade on update cascade 
--);

--CREATE TABLE PivotAllergen
--(
--  AllergenID INT NOT NULL,
--  FoodID INT NOT NULL,
--  FOREIGN KEY (AllergenID) REFERENCES Allergens(AllergenID),
--  FOREIGN KEY (FoodID) REFERENCES Menu(FoodID)
--  on delete cascade on update cascade 
--);

--CREATE TABLE PivotSize
--(
--  SizeID INT NOT NULL,
--  FoodID INT NOT NULL,
--  FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID),
--  FOREIGN KEY (FoodID) REFERENCES Menu(FoodID)
--  on delete cascade on update cascade 
--);

--CREATE TABLE DailyMenu
--(
--  DailyMenuID INT NOT NULL,
--  Date DATE NOT NULL,
--  DayOfWeek VARCHAR(50) NOT NULL,
--  PRIMARY KEY (DailyMenuID)
--);

--CREATE TABLE PivotDailyMenu
--(
--  FoodID INT NOT NULL,
--  DailuMenuID INT NOT NULL,
--  FOREIGN KEY (FoodID) REFERENCES Menu(FoodID),
--  FOREIGN KEY (DailuMenuID) REFERENCES DailyMenu(DailyMenuID)
--  on delete cascade on update cascade 
--);


--INSERT INTO Category
--VALUES
--('Soup'),
--('Main Course'),
--('Salad'), 
--('Pizza')

--INSERT INTO Allergens
--VALUES
--('Gluten'),
--('Crustaceans'),
--('Eggs'),
--('Fish'),
--('Peanuts'),
--('Soya'),
--('Milk'),
--('Nuts'),
--('Celery'),
--('Mustard'),
--('Sesame'),
--('Sulphites'),
--('Lupin'),
--('Moluscs')

--INSERT INTO Sizes
--VALUES
--('Small'),
--('Medium'),
--('Large')

--INSERT INTO Menu
--VALUES
--('Chicken Noodle Soup', 1),
--('Tomato Soup', 1),
--('Onion Soup', 1),
--('Charred Chicken with Sweet Potatoes', 2),
--('Slow-Roasted Salmon with Porridge', 2),
--('Steak with Fries', 2),
--('Caesar Salad', 3),
--('Caprese Salad', 3),
--('Greek Salad', 3),
--('Pizza Romana', 4),
--('Pizza Quattro Formaggi', 4),
--('Pizza Hawaii', 4)

--INSERT INTO PivotAllergen
--VALUES
--(1,1),
--(1,3),
--(2,8),
--(3,6)

--INSERT INTO PivotSize
--VALUES
--(1,1),
--(2,1),
--(3,1),
--(2,2),
--(3,2)

--INSERT INTO DailyMenu
--VALUES
--('2020-11-30', 'Monday'),
--('2020-12-01', 'Tuesday'),
--('2020-12-02', 'Wednesday'),
--('2020-12-03', 'Thursday'),
--('2020-12-04', 'Friday'),
--('2020-12-05', 'Saturday'),
--('2020-12-06', 'Sunday')

--INSERT INTO PivotDailyMenu
--VALUES
--(1,1),
--(4,1),
--(7,1),
--(10,1)

--ALTER TABLE Menu
--ADD Price float

--n.1
--SELECT Name, Price FROM Menu

--n.2
--SELECT Min(Price) AS CheapestFood FROM Menu

--n.3
--SELECT DailyMenuID, DayOfWeek FROM DailyMenu
--WHERE Date = '2020-12-04'

--n.4
--SELECT FoodID FROM PivotAllergen
--WHERE AllergenID = 2

--n.5
--SELECT Name, Price FROM Menu
--WHERE CategoryID <> 1 and CategoryID <> 3

--n.6
--SELECT DayOfWeek as ServedThisDay from DailyMenu
--left join PivotDailyMenu
--on PivotDailyMenu.DailuMenuID = DailyMenu.DailyMenuID
--where PivotDailyMenu.FoodID = 7

--n.7
--SELECT m.Name, COUNT(AllergenID) AmountOfAllergens FROM Menu m INNER JOIN PivotAllergen PA ON m.FoodID = PA.FoodID
--GROUP BY Name

--n.8
--UPDATE Menu
--SET Price = Price + 0.2
--WHERE CategoryID = 4
--Select Name,Price from Menu
--where CategoryID = 4

--n.9
--DELETE FROM Menu
--where Price = NULL

--n.10
--SELECT Menu.Name, Allergens.Name from Menu
--INNER JOIN PivotAllergen on PivotAllergen.FoodID = Menu.FoodID
--INNER JOIN Allergens on Allergens.AllergenID = PivotAllergen.AllergenID

--n.11
--SELECT Menu.Name, DailyMenu.DayofWeek FROM Menu
--INNER JOIN PivotDailyMenu on PivotDailyMenu.FoodID = Menu.FoodID
--INNER JOIN DailyMenu on DailyMenu.DailyMenuID = PivotDailyMenu.DailuMenuID
--WHERE DailyMenu.Date > '2020-12-02'

--n.12
--SELECT TOP 5 Price, Menu.Name, Allergens.Name FROM Menu
--INNER JOIN PivotAllergen ON PivotAllergen.FoodID = Menu.FoodID
--INNER JOIN Allergens on Allergens.AllergenID = PivotAllergen.AllergenID
--WHERE Allergens.Name not like 'Gluten'
--ORDER BY Price DESC

--n.13
--SELECT Category, Name, Size FROM Category
--inner join Menu on Menu.CategoryID = Category.CategoryID
--inner join PivotSize on PivotSize.FoodID = Menu.FoodID
--left join Sizes on Sizes.SizeID = PivotSize.SizeID
--WHERE Sizes.Size = 'Small'

--n.14
--SELECT Menu.Name, DayOfWeek, DailyMenu.Date FROM Menu
--INNER JOIN PivotDailyMenu ON PivotDailyMenu.FoodID = Menu.FoodID
--INNER JOIN DailyMenu ON DailyMenu.DailyMenuID = PivotDailyMenu.DailuMenuID
--INNER JOIN PivotAllergen ON PivotAllergen.FoodID = Menu.FoodID
--RIGHT JOIN Allergens ON Allergens.AllergenID = PivotAllergen.AllergenID
--WHERE Allergens.Name not like 'Milk'

--n.15
--SELECT Category, AVG(Price) Price FROM Category
--INNER JOIN Menu ON Menu.CategoryID = Category.CategoryID
--GROUP BY Category

--n.16
--SELECT Name,Price FROM Menu WHERE Price > 5
--INTERSECT
--SELECT Name,Price FROM Menu WHERE Price < 7


--n.17
--SELECT SUM(Price) AS AllInCategory, Category
--FROM Category
--INNER JOIN Menu ON Menu.CategoryID = Category.CategoryID
--GROUP BY Category
