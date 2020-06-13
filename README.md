# Deloitte Hackathon: MedConnect
Quick ReadMe:
MEDCONNECT was created by Julian Garratt, Aimen Hamed, and Hossion Ali. To run the main program use 'python3 server.py'. 
If 4 or 5 is used while the program is running you should be prompted with '[*] Waiting to connect to patient'.
At this point run 'python3 client.py' on a seperate terminal. You should then recieve 'Got connection from ...'.
Any issues or bugs please contact Julian Garratt.

Note: pandas is an external library please download via 'python3 -m pip install pandas'

Outline: 
  The purpose of this project is to provide quick and direct medical access to people who may live far away from hospitals or HPs,
  and also for people who need constant updates from a medical professional. MedConnect allows medical professionals
  to send immediate updates to patients via a wrist watch bridging the connection between patient and doctor.
  
Viability/Feasability: This project works towards creating a system where doctors are able to send or set periodic reminders for patients who live far away from hospitals in regards to their medication and respective dose frequency. This project does seem to be viable however more time would be necessary in order to fully implement the system with as many features and error checking as possible. With more time, a fully fledged program can be produced and used commercially with current technologies available today. 

Social Impact: By having such a program created it would allow another layer of communication between patient and doctor. With constant, automated reminders sent to a patient, it increases medication adherence and with the dose amount being mentioned as well, reduce the chance of an over/under dose. Implementing this program would allow people who live far away from hospitals or a GP, to receive consistent data on their medication plan, directly to a wearable wrist watch. One of the most common reasons for not adhering to prescribed medication is forgetfulness (Vervloet et al. 2012). Another study published by Vervloet et al later that year investigated the effectiveness of consistent SMS reminders for patients with type 2 diabetes. Her study divided 104 patients into two groups where one group received SMS reminders and the other did not. The results show that those who received consistent SMS reminders "significantly more doses within predefined time windows" as well as "miss doses less frequently". Further studies have been made into the effectiveness of reminders in regards to medication adherence and the general consensus from all the studies is that reminders are essential in ensuring medical adherence however SMS reminders could be implemented better (Liu et al. 2015; Mohammed, Glennerster and Khan, 2016). By having a wearable wrist watch that would be consistently worn by the patient, similar to a fitbit, patients would be able to receive reminders whenever they are sent by the system. Overall such a program would have immense social advantages are patients are no longer left wondering when and how much of their medication they are supposed to be taking.        

How it works: The product utilises a server-client based environment between a patient and the patient's doctor from which doctors are able to send and set periodic reminders to patients in regards to their respective medication and dose frequency. The connection between patient and doctor would be one way, from doctor to patient. These reminders would be sent to a wrist watch that the patient wears, similar to a pager. On the server end (ie doctors end), doctors would be able to enter patient details such as 'name', 'location', 'medication', 'dose size' and 'dose frequency'. This is then passed into a csv file from where doctors are then able to either send a reminder that instance or set up a scheduleded reminder at a specific time. There will be 6 functions that can be called upon by the doctor once in the menu screen of the server; 'Show clients', 'Add patients', 'Remove patients', 'Send reminder to patient', 'Send scheduled reminder to patient' and 'Exit', all explained below:
  'Show client' will print out the current list of patients that have been entered.
  'Add patient' will add a new patient using the details stated above.
  'Remove patient' will remove a specific patient from the current database
  'Send reminder to patient' will send a reminder to a specific at the current time
  'Send scheduled reminder to patient' will send a periodic reminder to a patient at a specified time.
  'Exit' will exit the program.




References

Liu, X., Lewis, J. J., Zhang, H., Lu, W., Zhang, S., Zheng, G., . . . Fielding, K. L. (2015). Effectiveness of Electronic Reminders to Improve Medication Adherence in Tuberculosis Patients: A Cluster-Randomised Trial. PLOS Medicine, 12(9), e1001876. doi:10.1371/journal.pmed.1001876

Mohammed, S., Glennerster, R., & Khan, A. J. (2016). Impact of a Daily SMS Medication Reminder System on Tuberculosis Treatment Outcomes: A Randomized Controlled Trial. PloS one, 11(11), e0162944-e0162944. doi:10.1371/journal.pone.0162944

Vervloet, M., Linn, A. J., van Weert, J. C. M., de Bakker, D. H., Bouvy, M. L., & van Dijk, L. (2012). The effectiveness of interventions using electronic reminders to improve adherence to chronic medication: a systematic review of the literature. Journal of the American Medical Informatics Association, 19(5), 696-704. doi:10.1136/amiajnl-2011-000748

Vervloet, M., van Dijk, L., Santen-Reestman, J., van Vlijmen, B., van Wingerden, P., Bouvy, M. L., & de Bakker, D. H. (2012). SMS reminders improve adherence to oral medication in type 2 diabetes patients who are real time electronically monitored. International Journal of Medical Informatics, 81(9), 594-604. doi:https://doi.org/10.1016/j.ijmedinf.2012.05.005
