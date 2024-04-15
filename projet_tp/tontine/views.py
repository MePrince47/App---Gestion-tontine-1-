from django.shortcuts import render,HttpResponseRedirect
from .forms import New_tontine
from .forms import New_membre
from .models import La_tontine
from .models import Le_membre
# Create your views here.
def home_page(request):
	return render(request,'index.html')	 

#Tontine
#fonction d'ajout en BD
def add_show(request):
	stud = La_tontine.objects.all()
	trouve = False
	if request.method =='POST':
		fm = New_tontine(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['nom']
			sn = fm.cleaned_data['slogan']
			re = fm.cleaned_data['regle']
			for val in stud:
				if val.nom == nm:
					trouve = True
			if trouve == False:
				reg=La_tontine(nom = nm,slogan=sn,regle=re)
				reg.save()
				fm=New_tontine()

	else:
		fm =New_tontine()
	stud = La_tontine.objects.all()
	return render(request,'tontine/add.html',{'form':fm, 'stu':stud, 'erreur':trouve})	 

#Fonction pour modifier les infos	

def modifier(request, id):
	if request.method == 'POST':
		pi = La_tontine.objects.get(pk=id)
		fm = New_tontine(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		pi = La_tontine.objects.get(pk = id)
		fm = New_tontine(instance = pi)
	return render(request,'tontine/update.html',{'form':fm})	 


	#fonction de suppression en BD
def suppression(request,id):
	if request.method == 'POST':
		pi = La_tontine.objects.get(pk = id)
		pi.delete()
		return HttpResponseRedirect('../')
#Membre  
def add_show_membre(request):
	trouve = False
	ton = La_tontine.objects.all()
	if request.method =='POST':
		fm = New_membre(request.POST) 
		trouve = True
		for val in ton:	
			if fm.is_valid():
			
				nm = fm.cleaned_data['nom']
				pr = fm.cleaned_data['Prénom']
				em = fm.cleaned_data['Email']
				tt = fm.cleaned_data['tontine']
				np = fm.cleaned_data['Nombre_parts']
				st = fm.cleaned_data['statut']
				if tt == val.nom:
					reg=Le_membre(nom = nm,Prénom=pr,Email=em,tontine=tt,Nombre_parts=np,statut=st)
					reg.save()
					fm=New_membre()
					trouve = False

	else:
		fm =New_membre()
	stud = Le_membre.objects.all()
	return render(request,'membre/add_membre.html',{'form1':fm, 'stu1':stud, 'erreur':trouve})	



#Fonction pour modifier les infos	

def modifier_membre(request, id):
	if request.method == 'POST':
		pi = Le_membre.objects.get(pk=id)
		fm = New_membre(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		pi = Le_membre.objects.get(pk = id)
		fm = New_membre(instance = pi)
	return render(request,'membre/update_membre.html',{'form':fm})	 


	#fonction de suppression en BD
def suppression_membre(request,id):
	if request.method == 'POST':
		pi = Le_membre.objects.get(pk = id)
		pi.delete()
		return HttpResponseRedirect('../')