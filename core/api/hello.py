from flask import Blueprint, render_template, request

from core.extensions import db
from core.models.stack import Stack

stack_router = Blueprint('stack', __name__)


@stack_router.route("/create_stack", methods=["POST"])
def create_stack():
    """
    Create stack
    """
    stack = Stack()
    db.session.add(stack)
    db.session.commit()
    return stack.get_json()


@stack_router.route("/add_element/<_id>", methods=["POST"])
def add_element_stack(_id):
    """
    Add element to stack
    """
    args = request.args

    if "value" in request.args:
        stack = Stack().query.filter_by(id=_id).first()

        if stack:
            if stack.value:
                new = stack.value + [float(args["value"])]
                stack.value = new
            else:
                stack.value = [float(args["value"])]
            db.session.commit()

            return stack.get_json()
        return {
            "message": "Stack id not found"
        }
    return {"message": "Missing argument value"}


@stack_router.route("/get_stack/<stack_id>", methods=["GET"])
def get_stack(stack_id):
    """
    Get stack
    """
    stack = Stack().query.filter_by(id=stack_id).first()
    if stack:
        return {"stack_info": stack.get_json()}
    else:
        return {"stack_info": "Stack not found"}


@stack_router.route("/clean_stack/<stack_id>", methods=["DELETE"])
def clean_stack(stack_id):
    """
    Clean stack
    """
    stack = Stack().query.filter_by(id=stack_id).first()

    if stack:
        db.session.delete(stack)
        return {"Message": "Stack deleted"}
    else:
        return {"Message": "Stack not found"}


@stack_router.route("/operand_plus/<stack_id>", methods=["GET"])
def operand_plus(stack_id):
    """
    +
    """
    stack = Stack().query.filter_by(id=stack_id).first()
    if stack:
        last_val = stack.value[-1]
        previous_last_val = stack.value[-2]
        new_val = last_val + previous_last_val

        if stack.value[:-2]:
            new_list = stack.value[:-2] + [new_val]
            stack.value = new_list
            db.session.commit()
            print(stack.value, new_list, stack.value[:-2])
            return stack.get_json()
        else:
            return {"Message": "Not enough value"}
    else:
        return {"Message": "Stack not found"}


@stack_router.route("/operand_minus/<stack_id>", methods=["GET"])
def operand_minus(stack_id):
    """
    -
    """
    stack = Stack().query.filter_by(id=stack_id).first()
    if stack:
        last_val = stack.value[-1]
        previous_last_val = stack.value[-2]
        new_val = last_val - previous_last_val
        if stack.value[:-2]:
            new_list = stack.value[:-2] + [new_val]
            print(stack.value, new_list)
            stack.value = new_list
            db.session.commit()
            return stack.get_json()
        else:
            return {"Message": "Not enough value"}
    else:
        return {"Message": "Stack not found"}


@stack_router.route("/operand_multiple/<stack_id>", methods=["GET"])
def operand_multiple(stack_id):
    """
    *
    """
    stack = Stack().query.filter_by(id=stack_id).first()
    if stack:
        last_val = stack.value[-1]
        previous_last_val = stack.value[-2]
        new_val = last_val * previous_last_val
        if stack.value[:-2]:
            new_list = stack.value[:-2] + [new_val]
            print(stack.value, new_list)
            stack.value = new_list
            db.session.commit()
            return stack.get_json()
        else:
            return {"Message": "Not enough value"}
    else:
        return {"Message": "Stack not found"}


@stack_router.route("/operand_division/<stack_id>", methods=["GET"])
def operand_division(stack_id):
    """
    /
    """
    stack = Stack().query.filter_by(id=stack_id).first()
    if stack:
        last_val = stack.value[-1]
        previous_last_val = stack.value[-2]
        new_val = last_val / previous_last_val
        if stack.value[:-2]:
            new_list = stack.value[:-2] + [new_val]
            print(stack.value, new_list)
            stack.value = new_list
            db.session.commit()
            return stack.get_json()
        else:
            return {"Message": "Not enough value"}
    else:
        return {"Message": "Stack not found"}
