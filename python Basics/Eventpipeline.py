'''
Problem 3 — Hard — Event Pipeline
Build create_pipeline(service_name, allowed_events) jo ek process(user_id, event_type, payload) function return kare.
Requirements:

Validate karo — user_id string hona chahiye, empty nahi, None nahi

event_type allowed set mein hona chahiye — nahi toh {"status": "rejected", "reason": "unknown event"}
payload ek dict hona chahiye — nahi toh TypeError
match/case se event type handle karo:

"signup" — payload mein email hona chahiye — store karo user
"purchase" — payload mein amount hona chahiye — track karo total revenue
"logout" — user ko active users se hataao


Track karo nonlocal se: total events, total rejected, total revenue, active users (set)
Ek generator attach karo process.get_events(event_type) jo sirf us type ke events yield kare
Last 200 events store karo — slicing se cap karo

Test karna hai:
pipeline = create_pipeline(
    service_name="myapp",
    allowed_events={"signup", "purchase", "logout"}
)

print(pipeline("u1", "signup", {"email": "u1@gmail.com"}))
print(pipeline("u1", "purchase", {"amount": 499.99}))
print(pipeline("u2", "signup", {"email": "u2@gmail.com"}))
print(pipeline("u1", "logout", {}))
print(pipeline("u1", "hack", {"evil": True}))   # rejected

purchases = list(pipeline.get_events("purchase"))
print(purchases)
'''

def create_pipeline(service_name, allowed_events):
    allowed_events={"signup", "purchase", "logout"}
    total_events=0
    total_rejected=0
    total_revenue=0
    active_users=set()
    all_events=[]
    
    def process(user_id, event_type, payload):
        nonlocal total_events, total_rejected, total_revenue, active_users, all_events
        if user_id is None or user_id == "" or not isinstance(user_id, str):
            raise KeyError("user_id must be a non-empty string")
        
        if event_type not in allowed_events:
            return {
                "status":"rejected",
                "reason":"unknown event occured"
            }
        
        if not isinstance(payload , dict):
            raise TypeError("Payload should be a dictionary")
        
        total_events += 1
        match event_type:
            case "signup":
                if "email" not in payload:
                    total_rejected += 1
                    return {"status": "rejected", "reason": "email missing"}
                active_users.add(user_id)
                event_record = {"user_id": user_id, "event_type": event_type, "payload": payload}
                all_events.append(event_record)
                return {"status": "success", "action": "user signed up"}
            
            case "purchase":
                if "amount" not in payload:
                    total_rejected += 1
                    return {"status": "rejected", "reason": "amount missing"}
                total_revenue += payload["amount"]
                event_record = {"user_id": user_id, "event_type": event_type, "payload": payload}
                all_events.append(event_record)
                return {"status": "success", "action": "purchase tracked"}
            
            case "logout":
                active_users.discard(user_id)
                event_record = {"user_id": user_id, "event_type": event_type, "payload": payload}
                all_events.append(event_record)
                return {"status": "success", "action": "user logged out"}
    
    def get_events(event_type):
        for event in all_events[-200:]:
            if event["event_type"] == event_type:
                yield event
    
    process.get_events = get_events
    return process


