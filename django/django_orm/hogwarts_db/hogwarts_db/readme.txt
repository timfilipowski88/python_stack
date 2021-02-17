INSERT INTO Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');

Wizard.objects.create(name="Harry Potter", house="Gryffindor", pet="Hedwig", year="5")


INSERT INTO Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');

Wizard.objects.create(name="Hermione Granger", house="Gryffindor", pet="Crookshanks", year="5")


SELECT * FROM Wizard WHERE id = 1;

Wizard.objects.filter(id="1")


SELECT * FROM Wizard WHERE house = 'Gryffindor';

Wizard.ojects.filter(house="Gryffindor")


UPDATE Wizard SET year = '6' WHERE id = 1;

wizard_update = Wizard.objects.get(id="1")
wizard_update.year = "6"
wizard.update.save()


Wizard.objects.create(name="Luna Lovegood", house="Ravenclaw", pet="None", year="4")copy

INSERT INTO Wizard (name, house, pet, year) VALUES ("Luna Lovegood", "Ravenclaw", "None", "4");


Wizard.objects.create(name="Padma Patil", house="Ravenclaw", pet="None", year="5")

INSERT INTO Wizard (name, house, pet, year) VALUES ("Padma Patil", "Ravenclaw, "None", "5");


ravenclaws = Wizard.objects.filter(house="Ravenclaw")

SELECT * FROM Wizard WHERE house = "Ravenclaw";


luna = Wizard.objects.get(name="Luna Lovegood")
luna.year = 5
luna.save()

UPDATE Wizard SET year = 5 WHERE name = "Luna Lovegood";

