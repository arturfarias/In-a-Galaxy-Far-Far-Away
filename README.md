#  Projeto The Force (Nome provisorio)  #

### Depêndencias ###

* Python 2.7.11
* Django 1.7.5
* Bootstrap 3
* bootstrap-form

### Modificações ###

* 26/jun/2016: Criado banco de dados no arquivo login/models.py.

* 27/jun/2016: Criado um novo banco de dados na forma de uma extenção do Perfil
do usuario cadastrado.

* 27/jun/2016: Criado tela de login simples.

* 27/jun/2016: Criado tela de cadastro simples.

* 27/jun/2016: Implementado redirecionamento para a pagina de login caso o
usuario não esteja logado

* 28/jun/2016: Criado Tela de perfil não editavel

* 03/ago/2016: Criado modelo de form para usado em cunjunto do casdastro de usuario e modificado varios outros

* 04/ago/2016: Reformulado o formulario de cadastro de usuarios, implementado a opção de logout do sistema

* 09/ago/2016: Personalizado o templete provisorio da tela de login (index), index tounou-se um templete independente do base e outros detalhes simples, adicionado o link para uso do admin do django

* 10/ago/2016: Remorido e corrigido pequenos deifeitos do index, adicionado o cadastro de laboratorios no admin base do django

* 16/ago/2016: Removido modelo de banco de dados que estava sem uso, adicionado perfil do usuario e possibilidade de mudar os dados. Criado nova aplicação para o admin. Novo banco de dados. Criado sistema de troca de senha (bug de mostrar por padrão a senha antiga foi detectado ). Resolvido bug que dava erro ao clicar em um link de um local diferente do padrão.

* 17/ago/2016: Modificado formularios usando bootstrap, pequenos erros corigidos, modificados alguns aspectos da aparencia do projeto 
