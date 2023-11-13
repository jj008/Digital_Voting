from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Voters, Candidates, Election, Votes, EC_Admins, Reports
from voter.models import Voted, Complain
import datetime

# Create your views here.
@login_required(login_url='home')
@staff_member_required(login_url='home')
def adminhome(request):
    adminhome.username = request.session['admin_id']
    try:
        a = EC_Admins.objects.get(ecadmin_id=adminhome.username)
        adminhome.adminimage = a.ecadmin_image
        return render(request,'admin/adminhome.html',{'username':adminhome.username,'image':adminhome.adminimage})
    except:
        messages.info(request, 'Add admin details in EC_Admins table')
        return render(request, 'index.html')


@login_required(login_url='home')
@staff_member_required(login_url='home')
def adminprofile(request):
    username = request.session['admin_id']
    a = EC_Admins.objects.get(ecadmin_id=username)
    ecadmin_id = a.ecadmin_id
    firstname = a.firstname
    lastname = a.lastname
    middlename = a.middlename
    gender = a.gender
    dateofbirth = a.dateofbirth
    address = a.address
    pincode = a.pincode
    mobile_no = a.mobile_no
    email = a.email
    adminimage = a.ecadmin_image
    return render(request,'admin/adminprofile.html',{'username':username, 'firstname':firstname, 'lastname':lastname, 'middlename':middlename, 'gender':gender, 'dob':dateofbirth, 'address':address, 'pincode':pincode, 'mob':mobile_no, 'email':email, 'image':adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def addvoter(request):
    return render(request, 'admin/addvoter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def add_voter(request):
    if (request.method == 'POST'):
        voterid_no = request.POST['vid']
        name = request.POST['name']
        father_name = request.POST['fname']
        gender = request.POST['gender']
        dateofbirth = request.POST['dob']
        address = request.POST['address']
        mobile_no = request.POST['mno']
        state = request.POST['state']
        pincode = request.POST['pincode']
        parliamentary = request.POST['ParliamentaryConstituency']
        assembly = request.POST['AssemblyConstituency']
        voter_image = request.FILES['vphoto']
        if (Voters.objects.filter(voterid_no=voterid_no).exists()):
            messages.info(request, 'voter id already registered')
            return render(request, 'admin/addvoter.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            add_voter = Voters(voterid_no=voterid_no, name=name, father_name=father_name, gender=gender,
                               dateofbirth=dateofbirth, address=address, mobile_no=mobile_no, state=state,
                               pincode=pincode, parliamentary=parliamentary, assembly=assembly, voter_image=voter_image)
            add_voter.save()
            messages.info(request, 'voter added')
            return render(request, 'admin/addvoter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def addcandidate(request):
    return render(request, 'admin/add candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def add_candidate(request):
    if request.method == 'POST':
        candidate_id = request.POST['cid']
        name = request.POST['name']
        father_name = request.POST['fname']
        gender = request.POST['gender']
        dateofbirth = request.POST['dob']
        address = request.POST['address']
        mobile_no = request.POST['mno']
        state = request.POST['state']
        pincode = request.POST['pincode']
        constituency = request.POST['Constituency']
        if constituency == "Parliamentary":
            parliamentary = request.POST['Constituency1']
        else:
            assembly = request.POST['Constituency1']
        candidate_party = request.POST['party']
        candidate_image = request.FILES['cphoto']
        party_image = request.FILES['pphoto']
        affidavit = request.FILES['affidavit']
        if (Candidates.objects.filter(candidate_id=candidate_id).exists()):
            messages.info(request, 'candidate id already registered')
            return render(request, 'admin/add candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            if constituency == "Parliamentary":
                add_candidate = Candidates(candidate_id=candidate_id, name=name, father_name=father_name, gender=gender,
                                           dateofbirth=dateofbirth, address=address, mobile_no=mobile_no, state=state,
                                           pincode=pincode, constituency=constituency, parliamentary=parliamentary,
                                           candidate_party=candidate_party, candidate_image=candidate_image,
                                           party_image=party_image,affidavit=affidavit)
                add_candidate.save()
            else:
                add_candidate = Candidates(candidate_id=candidate_id, name=name, father_name=father_name, gender=gender,
                                           dateofbirth=dateofbirth, address=address, mobile_no=mobile_no, state=state,
                                           pincode=pincode, constituency=constituency, assembly=assembly,
                                           candidate_party=candidate_party, candidate_image=candidate_image,
                                           party_image=party_image,affidavit=affidavit)
                add_candidate.save()
            messages.info(request, 'candidate added')
            return render(request, 'admin/add candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def generateelection(request):
    return render(request, 'admin/generateelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def generate_election(request):
    if request.method == 'POST':
        election_id = request.POST['eno']
        election_type = request.POST['electiontype']
        state = request.POST['state']
        start_date = request.POST['sdate']
        start_time = request.POST['stime']
        end_date = request.POST['edate']
        end_time = request.POST['etime']
        status = 'active'
        if (Election.objects.filter(election_id=election_id).exists()):
            messages.info(request, 'election id already registered')
            return render(request, 'admin/generateelection.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            generate_election = Election(election_id=election_id, election_type=election_type, state=state,
                                         start_date=start_date, start_time=start_time, end_date=end_date,
                                         end_time=end_time,
                                         status=status)
            generate_election.save()
            if election_type == 'PC-GENERAL':
                c = Candidates.objects.filter(state=state, constituency='Parliamentary')
                for i in c:
                    candidates_votes = Votes(election_id=election_id, candidate_id=i.candidate_id,
                                             candidate_name=i.name, candidate_party=i.candidate_party, state=i.state,
                                             constituency=i.parliamentary)
                    candidates_votes.save()
                has_voted = 'no'
                #Voted.objects.filter(state=state).delete()
                v = Voters.objects.filter(state=state)
                for i in v:
                    voters_voted = Voted(election_id=election_id, voter_id=i.voterid_no, state=i.state, constituency=i.parliamentary,
                                         has_voted=has_voted)
                    voters_voted.save()
                messages.info(request, 'election generated')
                return render(request, 'admin/generateelection.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                c = Candidates.objects.filter(state=state, constituency='Assembly')
                for i in c:
                    candidates_votes = Votes(election_id=election_id, candidate_id=i.candidate_id,
                                             candidate_name=i.name, candidate_party=i.candidate_party, state=i.state,
                                             constituency=i.parliamentary)
                    candidates_votes.save()
                has_voted = 'no'
                #Voted.objects.filter(state=state).delete()
                v = Voters.objects.filter(state=state)
                for i in v:
                    voters_voted = Voted(election_id=election_id, voter_id=i.voterid_no, state=i.state, constituency=i.assembly,
                                         has_voted=has_voted)
                    voters_voted.save()
                messages.info(request, 'election generated')
                return render(request, 'admin/generateelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def voting(request):
    return render(request, 'admin/voting.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def votervotesub(request):
    if request.method == 'POST':
        election_id = request.POST['eid']
        vid = request.POST['vid']
        if (Voted.objects.filter(election_id=election_id, voter_id=vid).exists()):
            v = Voted.objects.get(election_id=election_id, voter_id=vid)
            if v.has_voted == 'no':
                v.has_voted = 'yes'
                v.where_voted = 'offline'
                v.datetime = datetime.datetime.now()
                v.save()
                messages.info(request, 'Vote submitted')
                return render(request, 'admin/voting.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'Already voted')
                return render(request, 'admin/voting.html',{'username':adminhome.username,'image':adminhome.adminimage, 'where':v.where_voted})
        else:
            messages.info(request, 'voter not found')
            return render(request, 'admin/voting.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def completeelection(request):
    if Election.objects.filter(status='active'):
        e=Election.objects.filter(status='active')
        return render(request, 'admin/completeelection.html', {'elections': e,'username':adminhome.username,'image':adminhome.adminimage})
    else:
        messages.info(request, 'No elections running')
        return render(request, 'admin/completeelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def complete_election(request):
    if request.method == 'POST':
        election_id = request.POST['eno']
        status = 'active'
        e = Election.objects.get(election_id=election_id, status=status)
        if e is not None:
            e.status = 'not active'
            e.save()
            messages.info(request, 'Election Completed')
            return render(request, 'admin/completeelection.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            messages.info(request, 'Election already completed')
            return render(request, 'admin/completeelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def modifyelection(request):
    if Election.objects.filter(status='active'):
        e=Election.objects.filter(status='active')
        return render(request, 'admin/modifyelection.html', {'elections': e,'username':adminhome.username,'image':adminhome.adminimage})
    else:
        messages.info(request, 'No elections running')
        return render(request, 'admin/modifyelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def modify_election(request):
    if request.method == "POST":
        election_id=request.POST['eno']
        end_date=request.POST['edate']
        end_time=request.POST['etime']
        modifyele=Election.objects.get(election_id=election_id)
        modifyele.end_date=end_date
        modifyele.end_time=end_time
        modifyele.save()
        messages.info(request,'Election Modified')
        return render(request,'admin/modifyelection.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def generateresult(request):
    return render(request, 'admin/generateresult.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewcandidatesforaddvote(request):
    if request.method == 'POST':
        viewcandidatesforaddvote.election_id = request.POST['eno']
        state = request.POST['states']
        constituency = request.POST['constituency2']
        candidates = Votes.objects.filter(election_id=viewcandidatesforaddvote.election_id, state=state,
                                          constituency=constituency)
        return render(request, 'admin/addevmvotes.html', {'candidates': candidates,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def submitevmvote(request):
    candidate_id = request.POST.getlist('candidateid')
    votes = request.POST.getlist('votes')
    j = 0
    for i in candidate_id:
        v = Votes.objects.get(election_id=viewcandidatesforaddvote.election_id, candidate_id=i)
        v.evm_votes += int(votes[j])
        v.save()
        j += 1
    v = Votes.objects.all()
    for k in v:
        k.total_votes = k.online_votes + k.evm_votes
        k.save()
    messages.info(request, 'EVM Vote submitted')
    return render(request, 'admin/addevmvotes.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewresult(request):
    elections = Election.objects.all()
    return render(request, 'admin/viewresult.html', {'elections': elections,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def view_result(request):
    if request.method=="POST":
        election_id = request.POST['e_id']
        resulttype = request.POST['resulttype']
        e=Election.objects.get(election_id=election_id)
        estate=e.state
        if resulttype=="partywise":
            result = Votes.objects.filter(election_id=election_id)
            v=Votes.objects.filter(election_id=election_id)
            constituencies=[]
            for i in v:
                if i.constituency not in constituencies:
                    constituencies.append(i.constituency)
            d=[]
            for i in constituencies:
                resultcon=Votes.objects.filter(election_id=election_id,constituency=i)
                maxi=0
                for i in resultcon:
                    if i.total_votes>maxi:
                        maxi=i.total_votes
                        d.append(i.candidate_party)
            parties=[]
            for k in v:
                if k.candidate_party not in parties:
                    parties.append(k.candidate_party)
            final={}
            for i in parties:
                c=d.count(i)
                final.update({i:c})
            par=[]
            won=[]
            for k,v in final.items():
                par.append(k)
                won.append(v)
            parwon=zip(par,won)
            total=0
            for i in won:
                total+=i
            return render(request, 'admin/viewpartywise.html', {'total':total,'parwon':parwon,'electionid': election_id,'state':estate,'username':adminhome.username,'image':adminhome.adminimage})
        elif resulttype=="constituencywise":
            v=Votes.objects.filter(election_id=election_id)
            constituencies=[]
            for i in v:
                if i.constituency not in constituencies:
                    constituencies.append(i.constituency)
            return render(request, 'admin/viewresultconwise.html', {'electionid':election_id,'state':estate,'constituency':constituencies,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def view_result_filter(request):
    if request.method=="POST":
        election_id = request.POST['e_id']
        constituency = request.POST['constituency']
        e=Election.objects.get(election_id=election_id)
        estate=e.state
        v=Votes.objects.filter(election_id=election_id)
        result = Votes.objects.filter(election_id=election_id, constituency=constituency)
        constituencies=[]
        for i in v:
            if i.constituency not in constituencies:
                constituencies.append(i.constituency)
        totalvotes=0
        totalonline=0
        totalevm=0
        for i in result:
            totalvotes+=i.total_votes
            totalonline+=i.online_votes
            totalevm+=i.evm_votes
        perofvotes=[]
        for i in result:
            per=(i.total_votes/totalvotes)*100
            percentage=float("{:.2f}".format(per))
            perofvotes.append(percentage)
        finalresult=zip(result,perofvotes)
        return render(request, 'admin/viewresultconwise.html', {'totalonline':totalonline,'totalevm':totalevm,'totalvotes':totalvotes,'result':finalresult,'electionid':election_id,'state':estate,'constituency':constituencies,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def generatereport(request):
    return render(request, 'admin/generatereport.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def generate_report(request):
    election_id = request.POST['eno']
    state = request.POST['states']
    constituency = request.POST['constituency2']
    if Voted.objects.filter(election_id=election_id, state=state, constituency=constituency):
        vvotedall=Voted.objects.filter(election_id=election_id, state=state, constituency=constituency)
        e_male=0
        e_female=0
        e_others=0
        e_total=0
        for i in vvotedall:
            e_total=e_total+1
        for i in vvotedall:
            vdetail=Voters.objects.get(voterid_no=i.voter_id)
            if vdetail.gender == 'Male':
                e_male=e_male+1
            elif vdetail.gender == 'Female':
                e_female=e_female+1
            elif vdetail.gender == 'Others':
                e_others=e_others+1
        has_voted='yes'
        if Voted.objects.filter(election_id=election_id, state=state, constituency=constituency, has_voted=has_voted):
            vvotedyes=Voted.objects.filter(election_id=election_id, state=state, constituency=constituency, has_voted=has_voted)
            v_male=0 
            v_female=0
            v_others=0
            v_total=0
            for i in vvotedyes:
                v_total=v_total+1
            for i in vvotedyes:
                vdetail=Voters.objects.get(voterid_no=i.voter_id)
                if vdetail.gender == 'Male':
                    v_male=v_male+1
                elif vdetail.gender == 'Female':
                    v_female=v_female+1
                elif vdetail.gender == 'Others':
                    v_others=v_others+1
            if e_male!=0:
                p_male=(v_male/e_male)*100
                poll_male=float("{:.2f}".format(p_male))
            else:
                p_male=0
                poll_male=float("{:.2f}".format(p_male))
            
            if e_female!=0:
                p_female=(v_female/e_female)*100
                poll_female=float("{:.2f}".format(p_female))
            else:
                p_female=0
                poll_female=float("{:.2f}".format(p_female))
            
            if e_others!=0:
                p_others=(v_others/e_others)*100
                poll_others=float("{:.2f}".format(p_others))
            else:
                p_others=0
                poll_others=float("{:.2f}".format(p_others))
            
            if e_total!=0:
                p_total=(v_total/e_total)*100
                poll_total=float("{:.2f}".format(p_total))
            else:
                p_total=0
                poll_total=float("{:.2f}".format(p_total))
            report=Reports(election_id=election_id, state=state, constituency=constituency, electors_male=e_male, electors_female=e_female, electors_others=e_others, electors_total=e_total, voters_male=v_male, voters_female=v_female, voters_others=v_others, voters_total=v_total, poll_male=poll_male, poll_female=poll_female, poll_others=poll_others, poll_total=poll_total)
            report.save()
            messages.info(request, 'report generated')
            return render(request, 'admin/generatereport.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            messages.info(request, 'no one voted')
            return render(request, 'admin/generatereport.html',{'username':adminhome.username,'image':adminhome.adminimage})
    else:
        messages.info(request, 'not found')
        return render(request, 'admin/generatereport.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewreport(request):
    elections = Election.objects.all()
    return render(request, 'admin/viewreport.html', {'elections': elections,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
def view_report(request):
    election_id = request.POST['e_id']
    constituency = request.POST['constituency2']
    report = Reports.objects.filter(election_id=election_id, constituency=constituency)
    elections = Election.objects.all()
    return render(request, 'admin/viewreport.html', {'report': report, 'elections':elections,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewcandidate(request):
    return render(request, 'admin/view candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def view_candidate(request):
    if request.method == 'POST':
        state = request.POST['states']
        constituency1 = request.POST['constituency1']
        constituency2 = request.POST['constituency2']
        if constituency1 == 'Parliamentary':
            candidates = Candidates.objects.filter(state=state, constituency=constituency1, parliamentary=constituency2)
            if candidates:
                return render(request, 'admin/view candidate.html', {'constituency':constituency2,'candidates': candidates,'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'No Candidate Found')
                return render(request, 'admin/view candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            candidates = Candidates.objects.filter(state=state, constituency=constituency1, assembly=constituency2)
            if candidates:
                return render(request, 'admin/view candidate.html', {'constituency':constituency2,'candidates': candidates,'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'No Candidate Found')
                return render(request, 'admin/view candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewvoter(request):
    return render(request, 'admin/view voter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def view_voter(request):
    if request.method == 'POST':
        state = request.POST['states']
        constituency1 = request.POST['constituency1']
        constituency2 = request.POST['constituency2']
        if constituency1 == 'Parliamentary':
            voters = Voters.objects.filter(state=state, parliamentary=constituency2)
            return render(request, 'admin/view voter.html', {'voters': voters,'username':adminhome.username,'image':adminhome.adminimage})
        else:
            voters = Voters.objects.filter(state=state, assembly=constituency2)
            return render(request, 'admin/view voter.html', {'voters': voters,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def editvoter(request):
    return render(request, 'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def edit_voter(request):
    if request.method == 'POST':
        if request.POST.get('editvoter'):
            voter_id = request.POST['vid']
            if Voters.objects.filter(voterid_no=voter_id):
                voter = Voters.objects.get(voterid_no=voter_id)
                return render(request, 'admin/edit voterdetails.html', {'voterid_no': voter.voterid_no, 'name': voter.name,
                                                                'father_name': voter.father_name, 'gender': voter.gender,
                                                                'dateofbirth': voter.dateofbirth, 'address': voter.address,
                                                                'mobile_no': voter.mobile_no, 'state': voter.state,
                                                                'pincode': voter.pincode,
                                                                'parliamentary': voter.parliamentary,
                                                                'assembly': voter.assembly, 'voter_image': voter.voter_image,'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request,'Voter not found')
                return render(request,'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})
        elif request.POST.get('deletevoter'):
            voter_id = request.POST['vid']
            if Voters.objects.filter(voterid_no=voter_id):
                Voters.objects.get(voterid_no=voter_id).delete()
                User.objects.get(username=voter_id).delete()
                messages.info(request, 'Voter deleted')
                return render(request, 'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request,'Voter not found')
                return render(request,'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def editvoterdetails(request):
    if request.method == 'POST':
        voterid_no = request.POST['vid']
        name = request.POST['name']
        father_name = request.POST['fname']
        address = request.POST['address']
        mobile_no = request.POST['mno']
        state = request.POST['state']
        pincode = request.POST['pincode']
        parliamentary = request.POST['ParliamentaryConstituency']
        assembly = request.POST['AssemblyConstituency']
        evoter = Voters.objects.get(voterid_no=voterid_no)
        evoter.name = name
        evoter.father_name = father_name
        evoter.address = address
        evoter.mobile_no = mobile_no
        evoter.state = state
        evoter.pincode = pincode
        evoter.parliamentary = parliamentary
        evoter.assmebly = assembly
        evoter.save()
        messages.info(request, 'voter details updated')
        return render(request, 'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def editcandidate(request):
    return render(request, 'admin/edit candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def edit_candidate(request):
    if request.method == 'POST':
        if request.POST.get('editcandidate'):
            candidate_id = request.POST['cid']
            if Candidates.objects.filter(candidate_id=candidate_id):
                candidate = Candidates.objects.get(candidate_id=candidate_id)
                if candidate.constituency == "Parliamentary":
                    return render(request, 'admin/edit candidatedetails.html',
                                {'candidate_id': candidate.candidate_id, 'name': candidate.name,
                                'father_name': candidate.father_name, 'gender': candidate.gender,
                                'dateofbirth': candidate.dateofbirth, 'address': candidate.address,
                                'mobile_no': candidate.mobile_no, 'state': candidate.state,
                                'pincode': candidate.pincode, 'constituency': candidate.constituency,
                                'parliamentary': candidate.parliamentary,
                                'candidate_image': candidate.candidate_image, 'candidate_party': candidate.candidate_party,
                                'party_image': candidate.party_image,'affidavit':candidate.affidavit,'username':adminhome.username,'image':adminhome.adminimage})
                else:
                    return render(request, 'admin/edit candidatedetails.html',
                                {'candidate_id': candidate.candidate_id, 'name': candidate.name,
                                'father_name': candidate.father_name, 'gender': candidate.gender,
                                'dateofbirth': candidate.dateofbirth, 'address': candidate.address,
                                'mobile_no': candidate.mobile_no, 'state': candidate.state,
                                'pincode': candidate.pincode, 'constituency': candidate.constituency,
                                'parliamentary': candidate.parliamentary,
                                'candidate_image': candidate.candidate_image, 'candidate_party': candidate.candidate_party,
                                'party_image': candidate.party_image,'affidavit':candidate.affidavit,'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'Candidate not found')
                return render(request, 'admin/edit candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})
        elif request.POST.get('deletecandidate'):
            candidate_id = request.POST['cid']
            if Candidates.objects.filter(candidate_id=candidate_id):
                candidate = Candidates.objects.get(candidate_id=candidate_id).delete()
                messages.info(request, 'Candidate deleted')
                return render(request, 'admin/edit candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'Candidate not found')
                return render(request,'admin/edit candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def editcandidatedetails(request):
    if request.method == 'POST':
        candidate_id = request.POST['cid']
        name = request.POST['name']
        father_name = request.POST['fname']
        address = request.POST['address']
        mobile_no = request.POST['mno']
        state = request.POST['state']
        pincode = request.POST['pincode']
        constituency = request.POST['Constituency']
        if constituency == "Parliamentary":
            parliamentary = request.POST['Constituency1']
        else:
            assembly = request.POST['Constituency1']
        candidate_party = request.POST['party']
        party_image = request.FILES['pphoto']
        ecandidate = Candidates.objects.get(candidate_id=candidate_id)
        ecandidate.name = name
        ecandidate.father_name = father_name
        ecandidate.address = address
        ecandidate.mobile_no = mobile_no
        ecandidate.state = state
        ecandidate.pincode = pincode
        ecandidate.constituency = constituency
        if constituency == "Parliamentary":
            ecandidate.parliamentary = parliamentary
        else:
            ecandidate.assembly = assembly
        ecandidate.candidate_party=candidate_party
        ecandidate.party_image=party_image
        ecandidate.save()
        messages.info(request, 'candidate details updated')
        return render(request, 'admin/edit candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewcomplain(request):
    if Complain.objects.filter(viewed=False, replied=False):
        allcomplain=Complain.objects.filter(viewed=False, replied=False)
        return render(request, 'admin/viewcomplain.html', {'complain': allcomplain,'username':adminhome.username,'image':adminhome.adminimage})
    else:
        messages.info(request,'No New Complains')
        return render(request, 'admin/viewcomplain.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def replycomplain(request):
    if Complain.objects.filter(viewed=False, replied=False):
        allcomplain=Complain.objects.filter(viewed=False, replied=False)
        return render(request, 'admin/replycomplain.html', {'complain': allcomplain,'username':adminhome.username,'image':adminhome.adminimage})
    else:
        messages.info(request,'No New Complains')
        return render(request, 'admin/viewcomplain.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def reply_complain(request):
    if request.method == "POST":
        complain_id=request.POST['complainid']
        reply=request.POST['replycomplain']
        complain=Complain.objects.get(id=complain_id)
        complain.complain_reply=reply
        complain.viewed=True
        complain.replied=True
        complain.save()
        allcomplain = Complain.objects.filter(viewed=False, replied=False)
        return render(request, 'admin/replycomplain.html',{'complainid':complain_id,'complain':allcomplain,'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def achangepassword(request):
    return render(request, 'admin/achangepassword.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def achange_password(request):
    if request.method == "POST":
        a_id = request.session['admin_id']
        oldpass = request.POST['oldpass']
        newpass = request.POST['password1']
        newpass2 = request.POST['password2']
        u=auth.authenticate(username=a_id,password=oldpass)
        if u is not None:
            u=User.objects.get(username=a_id)
            if oldpass!=newpass:
                if newpass == newpass2:
                    u.set_password(newpass)
                    u.save()
                    messages.info(request, 'Password Changed')
                    return render(request, 'admin/achangepassword.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'New password is same as old password')
                return render(request, 'admin/achangepassword.html',{'username':adminhome.username,'image':adminhome.adminimage})
        else:
            messages.info(request, 'Old Password not matching')
            return render(request, 'admin/achangepassword.html',{'username':adminhome.username,'image':adminhome.adminimage})