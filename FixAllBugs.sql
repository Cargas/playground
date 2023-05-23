create proc FixAllBugs
as
begin
    declare @EnergyHasBugs bit = 1

    while @EnergyHasBugs = 1
    begin
        delete bEntity
    end
end