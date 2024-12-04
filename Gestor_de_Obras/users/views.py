


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages

user_model = get_user_model()

# VIEW DE LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('home:home_index')  # Ajuste o redirecionamento conforme necessário
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# VIEW DE LOGOUT

def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu do sistema com sucesso.")
    return redirect('users:login_view')

# VIEW DE CREATE USER

from .forms import EngineerProfileForm

def create_user_view(request):
    if request.method == 'POST':
        # Captura dados do formulário padrão do Django User
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Estrutura de decisão para verificar se as senha coincidem:
        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'users/register.html',{
                'form': EngineerProfileForm(request.POST),
                'username': username,
                'email': email
            })
        
        # Criação do usuário Django / Variavel que armazena o modelo padrão de usuário atual do sistema
        user_model = get_user_model()

        # Verificar se o nome de usuário ou e-mail já estão em uso
        if user_model.objects.filter(username=username).exists():
            messages.error(request, "O nome de usuário já está em uso.")
            return render(request, 'users/register.html')

        if user_model.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso.")
            return render(request, 'users/register.html',{
                'form': EngineerProfileForm(request.POST),
                'username': username,
                'email': email
            })
        
        # Não precisa ser um Try... verificar se vai manter essa estrutura na view...
        try:
            user_created = user_model.objects.create_user(username=username, email=email, password=password) #objects é um gerenciador padrão do modelo Django. É uma interface para realizar operações no banco de dados, como criar, buscar, atualizar ou excluir objetos.
        except Exception as Exc:
            messages.error(request, f"Erro ao criar usuário: {str(Exc)}")
            return render(request, 'users/register.html', {
                'form': EngineerProfileForm(request.POST),
                'username': username,
                'email': email
            })

        # Captura os dados adicionais para o perfil
        form = EngineerProfileForm(request.POST) #Instanciando um objeto da classe com os dados enviados pelo usuário no POST, essa ação funcionará como ferramenta para validar e manipular os dados

        if form.is_valid():
            engineer_profile = form.save(commit=False) #O objeto é criado pelo metodo 'save', mas como o 'commit' aqui é falso, o objeto não é salvo automaticamente no banco de dados, permitindo que possam ser realizadas modificações no objeto antes de persistí-lo (dar commit). 
            #Nesse ponto, um objeto EngineerProfile é instanciado com os dados fornecidos pelo usuário, mas ele ainda não foi inserido no banco de dados.
            engineer_profile.user = user_created # O usuário que récem foi criado está armazenado na variavel 'user_created'. O objeto EngineerProfile criado é associado a esse usuario nesta linha, sendo uma relação OneToOneField (um para um). 
            #A linha engineer_profile.user = user_created preenche a chave estrangeira (user) do modelo EngineerProfile com o usuário recém-criado.
            engineer_profile.save()
            #Após associar o perfil ao usuário, o método save() é chamado para persistir o objeto engineer_profile no banco de dados. Agora, o perfil de engenheiro está salvo, e o relacionamento com o usuário é mantido.
            messages.success(request, f"Usuário {user_created.username} e o perfil {engineer_profile.nome}foram criados com sucesso!")

            print(f"O usuário {user_created.username} e o perfil {engineer_profile.nome} foram criados com sucesso!")
            return redirect('users:login_view')
        
        else:
            print(form.errors)
            messages.error(request, "Erro ao salvar o perfil. Verifique os dados.")
            messages.error(request, "As senhas precisam ser preenchidas novamente.")
            user_created.delete()  # Remove o usuário caso o perfil falhe.É importante notar que a exclusão de um registro não afeta o valor da sequência de incremento da PK; ela só afeta as linhas presentes na tabela.
        
    else:
        form = EngineerProfileForm()
    return render(request, 'users/register.html', 
                  {'form': form,
                   })

# VIEW para listar usuários criados na Home

def user_list_view(request):
    users = user_model.objects.all()
    return render(request, 'users/list.html', {'users': users})
