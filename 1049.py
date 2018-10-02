valores = {
	"vertebrado":{
		"ave":{
			"carnivoro":"aguia",
			"onivoro":"pomba"
		},
		"mamifero":{
			"onivoro":"homem",
			"herbivoro":"vaca"
		
		}
	},
	
	"invertebrado":{
		"inseto":{
			"hematofago":"pulga",
			"herbivoro":"lagarta"
		},
		"anelideo":{
			"hematofago":"sanguessuga",
			"onivoro":"minhoca"
		}
	}
	}
	


v1 = input()
v2 = input()
v3 = input()
print(valores[v1][v2][v3])