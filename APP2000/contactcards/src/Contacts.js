import Phone from "./images/phone-icon.png"
import Email from "./images/mail-icon.png"

export default function Contact(props) {
    return (
        <div className="contact-card">
            <img src={props.img} alt={props.name} />
                <h3>{props.name}</h3>
            <div className="info-group">
                <img src={Phone} alt="phone icon" />
                <p>{props.phone}</p>
            </div>
            <div className="info-group">
                <img src={Email} alt="email icon" />
                <p>{props.email}</p>
          </div>
        </div>
    )
}