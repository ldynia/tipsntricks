$user1 = 'xldyn'
$user2 = 'nitdy'

$u1g = Get-ADPrincipalGroupMembership $user1 | select name
$u2g = Get-ADPrincipalGroupMembership $user2 | select name
 
Compare-Object -ReferenceObject $u1g -DifferenceObject $u2g -IncludeEqual -PassThru -ExcludeDifferent | SELECT Name
