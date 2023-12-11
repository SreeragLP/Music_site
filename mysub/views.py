from django.shortcuts import render,redirect
from mysub.models import Account,Subscribe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

#Create your views here.
# @login_required
# def subscribe(request):
#     if(request.method=="POST"):
#         n=request.POST['n']
#         user=request.user
#         amount=99
#         try:
#             acct =Account.objects.get(accnumber=n)
#             if (acct.balance >= amount):
#                 acct.balance -= amount
#                 acct.save()
#                 s=Subscribe.objects.create(user=user,amount=amount)
#                 s.save()
#                 msg = 'subscribed successfully'
#                 return render(request,'subscribe/subscription_confirm.html',{'msg':msg })
#             else:
#                 msg="insufficient bank balance"
#                 return render(request,'subscribe/subscription_confirm.html',{'msg': msg})
#         except:
#
#             msg = "invalid acc number"
#             return render(request,'subscribe/subscription_confirm.html',{'msg': msg})
#
#     return render(request,'subscribe/subscribe.html')





@login_required
def subscribe(request):
    if request.method == "POST":
        n = request.POST['n']
        if not n:
            messages.error(request, 'You must type an account number')
            return render(request, 'subscribe/subscribe.html')


            # msg = 'You must type an account number'
            # return render(request, 'subscribe/subscription_confirm.html', {'msg': msg})

        user = request.user
        amount = 199

        # # Check if the user already has a subscription
        # existing_subscription = Subscribe.objects.filter(user=user).exists()
        #
        # if existing_subscription:
        #     # in case where the user already has a subscription
        #     msg = 'You are already subscribed'
        #     return render(request, 'subscribe/subscription_confirm.html', {'msg': msg})

        try:
            acct = Account.objects.get(accnumber=n)
            if acct.balance >= amount:
                acct.balance -= amount
                acct.save()
                s = Subscribe.objects.create(user=user, amount=amount)
                s.save()
                msg = 'Subscribed successfully'
                return render(request, 'subscribe/subscription_confirm.html', {'msg': msg})
            else:
                msg = "Insufficient bank balance"
                return render(request, 'subscribe/subscription_confirm.html', {'msg': msg})
        except Account.DoesNotExist:
            messages.error(request, 'Invalid account number')
            return render(request, 'subscribe/subscribe.html')
            #msg = "Invalid account number"
            # return render(request, 'subscribe/subscription_confirm.html')


    try:
        user = request.user

        try:

            existing_subscription = Subscribe.objects.get(user=user)

            if existing_subscription:
                return render(request,'subscribe/subscribe.html',{'existing_subscription': existing_subscription})

        except:
            return render(request, 'subscribe/subscribe.html.html')
    except:
        pass



    return render(request, 'subscribe/subscribe.html')



