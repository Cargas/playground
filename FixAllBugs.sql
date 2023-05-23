create proc FixAllBugs
as
begin
    declare @EnergyHasBugs bit = 1

    while @EnergyHasBugs = 1
    begin
        delete bEntity
    end

    exec msdb.dbo.sp_send_dbmail
        @profile_name = 'prof',
        @recipients = 'manager@cargas.com',
        @subject = 'Important Notification',
        @body = '<div style="centered">Alright boss. Fixed it.</div>',
        @body_format = 'HTML'
end