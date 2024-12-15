from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target=None):
    """
    Creates a notification.
    :param recipient: User who receives the notification
    :param actor: User who performs the action
    :param verb: Description of the action
    :param target: The object related to the action (optional)
    """
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target=target,
        target_content_type=ContentType.objects.get_for_model(target) if target else None,
        target_object_id=target.id if target else None,
    )
