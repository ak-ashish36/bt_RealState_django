from django.shortcuts import render,redirect
from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail
# import environ
# env = environ.Env()

def contact(request):
    if request.method == "POST" :
        listing = request.POST['listing']
        listing_id = request.POST['listing_id'] 
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
    
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an inquiry for this property")
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        
        # Send mail
        # send_mail(
        #     "Property Listing Inquiry",
        #     "There has been an inquiry for "+listing+". Sign into admin panel for more info",
        #     env("PERSONAL_EMAIL"),
        #     [realtor_email,env("PERSONAL_EMAIL2")],
        #     fail_silently=False
        # )
        messages.success(request, "Your request has been submitted,  a realtor will get back to you soon")
        
        return redirect('/listings/'+listing_id)
    return redirect('/listings/'+listing_id)